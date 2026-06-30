from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import (
    EcoAction,
    Friendship,
    EcoGroup,
    GroupMember,
    UserProfile,
    Badge,
    UserBadge,
    EcoActionLike,
    GroupWeeklyQuest,
    GroupInvite,
    DailyMission,
    UserDailyMission,
    WeeklyMission,
    UserWeeklyMission,
    AvatarFrame,
    UserAvatarFrame,
    UserGroupQuestReward,
    TriviaQuestion,
    UserTriviaSubmission,
    AICoachSuggestion,
)
from .utils import get_user_total_points


# ==========================================
# USER PROFILE & USER ADMIN INLINE
# ==========================================

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Eco Profile Info"
    fk_name = "user"


class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]
    list_display = ("username", "email", "is_staff", "get_points", "get_streak", "date_joined")
    list_select_related = ("profile",)

    def get_points(self, obj):
        return get_user_total_points(obj)
    get_points.short_description = "Total Points"

    def get_streak(self, obj):
        return obj.profile.streak_count if hasattr(obj, "profile") else 0
    get_streak.short_description = "Streak (Days)"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# ==========================================
# FEATURE MODEL ADMINS
# ==========================================

@admin.register(EcoAction)
class EcoActionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "category", "points", "created_at", "caption")
    list_filter = ("category", "created_at")
    search_fields = ("user__username", "caption", "category")
    raw_id_fields = ("user",)
    ordering = ("-created_at",)


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "receiver", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("sender__username", "receiver__username")
    actions = ["make_accepted"]

    @admin.action(description="Mark selected friendships as Accepted")
    def make_accepted(self, request, queryset):
        queryset.update(status="accepted")


@admin.register(EcoGroup)
class EcoGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "member_count", "created_at")
    search_fields = ("name", "owner__username")
    list_filter = ("created_at",)
    raw_id_fields = ("owner",)


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "user", "joined_at")
    search_fields = ("group__name", "user__username")
    list_filter = ("joined_at",)
    raw_id_fields = ("group", "user")


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "icon", "requirement_category", "requirement_count")
    search_fields = ("name", "code")
    list_filter = ("requirement_category",)


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "badge", "earned_at")
    search_fields = ("user__username", "badge__name")
    list_filter = ("earned_at",)
    raw_id_fields = ("user", "badge")


@admin.register(EcoActionLike)
class EcoActionLikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "action", "reaction_type", "created_at")
    search_fields = ("user__username", "action__id")
    list_filter = ("reaction_type", "created_at")
    raw_id_fields = ("user", "action")


@admin.register(GroupWeeklyQuest)
class GroupWeeklyQuestAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "category", "target_count", "start_date", "is_completed")
    list_filter = ("is_completed", "category", "start_date")
    search_fields = ("group__name",)
    raw_id_fields = ("group",)


@admin.register(GroupInvite)
class GroupInviteAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "sender", "receiver", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("group__name", "sender__username", "receiver__username")
    raw_id_fields = ("group", "sender", "receiver")


@admin.register(DailyMission)
class DailyMissionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "bonus_points", "is_active")
    list_filter = ("is_active", "category")
    search_fields = ("title",)


@admin.register(UserDailyMission)
class UserDailyMissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "mission", "date", "is_completed", "earned_points")
    list_filter = ("is_completed", "date")
    search_fields = ("user__username", "mission__title")
    raw_id_fields = ("user", "mission", "completed_action")


@admin.register(WeeklyMission)
class WeeklyMissionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "bonus_points", "is_active")
    list_filter = ("is_active", "category")
    search_fields = ("title",)


@admin.register(UserWeeklyMission)
class UserWeeklyMissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "mission", "start_date", "completed_count", "required_count", "is_completed", "earned_points")
    list_filter = ("is_completed", "start_date")
    search_fields = ("user__username", "mission__title")
    raw_id_fields = ("user", "mission")


@admin.register(AvatarFrame)
class AvatarFrameAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "cost", "preview_emoji")
    search_fields = ("name", "code")


@admin.register(UserAvatarFrame)
class UserAvatarFrameAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "frame", "purchased_at")
    search_fields = ("user__username", "frame__name")
    list_filter = ("purchased_at",)
    raw_id_fields = ("user", "frame")


@admin.register(UserGroupQuestReward)
class UserGroupQuestRewardAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "quest", "earned_points", "awarded_at")
    search_fields = ("user__username",)
    list_filter = ("awarded_at",)
    raw_id_fields = ("user", "quest")


@admin.register(TriviaQuestion)
class TriviaQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text", "correct_option")
    search_fields = ("question_text",)


@admin.register(UserTriviaSubmission)
class UserTriviaSubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "questions_answered", "correct_answers", "earned_points")
    list_filter = ("date",)
    search_fields = ("user__username",)
    raw_id_fields = ("user",)


@admin.register(AICoachSuggestion)
class AICoachSuggestionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "suggested_category", "suggestion_text")
    list_filter = ("date", "suggested_category")
    search_fields = ("user__username", "suggestion_text")
    raw_id_fields = ("user",)