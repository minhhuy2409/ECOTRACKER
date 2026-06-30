import logging
from celery import shared_task
from django.db import transaction
from django.core.cache import cache
from django.utils import timezone
from tracker.models import EcoAction
from tracker.ai_utils import classify_eco_image
from tracker.utils import update_user_streak, check_and_award_badges, complete_missions_for_action

logger = logging.getLogger(__name__)

@shared_task
def classify_eco_action_task(action_id):
    logger.info(f"Starting Celery Gemini AI classification for EcoAction ID: {action_id}")
    try:
        eco_action = EcoAction.objects.select_related("user").get(id=action_id)
    except EcoAction.DoesNotExist:
        logger.error(f"EcoAction ID {action_id} not found.")
        return f"EcoAction {action_id} not found."

    # Call the Gemini AI classifier
    ai_result = classify_eco_image(eco_action.image, eco_action.caption)

    # Apply database changes atomically to ensure points and milestones are consistent
    with transaction.atomic():
        # Re-fetch instance and lock row
        eco_action = EcoAction.objects.select_related("user").select_for_update().get(id=action_id)
        
        eco_action.ai_reason = ai_result["reason"]
        
        if ai_result["is_eco_action"]:
            eco_action.ai_status = "approved"
            eco_action.category = ai_result["category"]
            eco_action.save()

            # Update streak and multiplier
            streak_count, multiplier = update_user_streak(eco_action.user)
            if multiplier > 1.0:
                eco_action.points = int(eco_action.points * multiplier)
                eco_action.save()

            # Check and award badges
            check_and_award_badges(eco_action.user)

            # Complete and progress daily & weekly missions
            complete_missions_for_action(eco_action.user, eco_action)
            logger.info(f"EcoAction ID {action_id} successfully approved under category {eco_action.category}")
        else:
            eco_action.ai_status = "rejected"
            eco_action.save()
            logger.warning(f"EcoAction ID {action_id} rejected by AI. Reason: {eco_action.ai_reason}")

        # Invalidate the leaderboard cache
        cache.delete("leaderboard_data")

    return f"Action {action_id} processed. Status: {eco_action.ai_status}"
