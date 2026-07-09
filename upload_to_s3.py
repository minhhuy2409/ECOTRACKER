import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import os
import sys

def upload_image_to_s3(file_name, bucket, object_name=None):
    """
    Tải một file ảnh lên AWS S3 bucket.

    :param file_name: Đường dẫn tới file ảnh trên máy tính (VD: 'images/test.jpg')
    :param bucket: Tên S3 bucket (VD: 'my-ecotracker-bucket')
    :param object_name: Tên file khi lưu trên S3. Nếu không truyền, sẽ lấy tên gốc của file.
    :return: True nếu upload thành công, ngược lại là False.
    """
    
    # Nếu không truyền object_name, lấy tên từ file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Khởi tạo client s3
    # Boto3 sẽ tự động lấy thông tin xác thực từ biến môi trường (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY) 
    # hoặc file cấu hình ~/.aws/credentials
    s3_client = boto3.client('s3')

    try:
        print(f"Đang tiến hành tải file '{file_name}' lên bucket '{bucket}'...")
        
        # Để file ảnh hiển thị được trên trình duyệt, có thể cần thiết lập ContentType
        # Ở đây ta set sẵn một vài loại phổ biến. Bạn có thể dùng module `mimetypes` để tự động hóa.
        content_type = 'image/jpeg'
        if file_name.lower().endswith('.png'):
            content_type = 'image/png'
        elif file_name.lower().endswith('.webp'):
            content_type = 'image/webp'
            
        extra_args = {'ContentType': content_type}

        # Upload file
        s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=extra_args)
        
        print(f"✅ Tải lên thành công! File lưu tại S3: {object_name}")
        return True
        
    except FileNotFoundError:
        print(f"❌ Lỗi: Không tìm thấy file gốc '{file_name}' trên máy tính.")
        return False
    except NoCredentialsError:
        print("❌ Lỗi: Không tìm thấy AWS credentials. Vui lòng kiểm tra lại cấu hình tài khoản.")
        return False
    except PartialCredentialsError:
        print("❌ Lỗi: Thông tin AWS credentials chưa đầy đủ.")
        return False
    except ClientError as e:
        print(f"❌ Lỗi S3 Client: {e}")
        return False
    except Exception as e:
        print(f"❌ Lỗi không xác định: {e}")
        return False


if __name__ == "__main__":
    # Ví dụ cách sử dụng (Cập nhật đường dẫn file và tên bucket của bạn)
    
    # IMAGE_PATH = "đường_dẫn_tới_ảnh_của_bạn.jpg"
    # BUCKET_NAME = "tên_bucket_của_bạn"
    
    # # Kiểm tra xem đã có param truyền vào từ terminal chưa
    if len(sys.argv) == 3:
        IMAGE_PATH = sys.argv[1]
        BUCKET_NAME = sys.argv[2]
        upload_image_to_s3(IMAGE_PATH, BUCKET_NAME)
    else:
        print("Sử dụng: python upload_to_s3.py <đường_dẫn_file> <tên_bucket>")
        print("Ví dụ: python upload_to_s3.py avatar.png my-ecotracker-bucket")
