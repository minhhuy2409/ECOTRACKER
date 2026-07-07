from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    """Lưu media files (avatar, eco action images) vào thư mục media/ trên S3."""
    location = "media"
    file_overwrite = False
