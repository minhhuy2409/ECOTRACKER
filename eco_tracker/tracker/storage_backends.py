from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    """
    Custom S3 storage backend for media files.
    All uploads (avatars, eco action images) will be stored
    under the 'media/' prefix in the S3 bucket.

    Example S3 paths:
      - media/avatars/user123.jpg
      - media/eco_actions/action456.png
    """
    location = "media"
    file_overwrite = False
