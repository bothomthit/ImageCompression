import os
import time
from osgeo import gdal

def compress_to_webp_lossless(input_file, output_file):
    # Mở tệp ảnh gốc
    dataset = gdal.Open(input_file)

    # Kiểm tra xem tệp đã mở thành công
    if dataset is None:
        print("Không thể mở tệp ảnh.")
        return

    # Lấy kích thước tệp trước khi nén
    original_size = os.path.getsize(input_file)

    # Tạo tham số cấu hình cho nén WebP lossless
    options = ["LOSSLESS=YES"]

    # Bắt đầu tính thời gian
    start_time = time.time()

    # Nén và lưu tệp dưới định dạng WebP
    gdal.Translate(output_file, dataset, format='WEBP', options=options)

    # Giải phóng bộ nhớ
    dataset = None

    # Tính toán thời gian nén
    end_time = time.time()
    compression_time = end_time - start_time

    # Lấy kích thước tệp sau khi nén
    compressed_size = os.path.getsize(output_file)

    # Tính phần trăm dung lượng giảm
    reduction_percentage = ((original_size - compressed_size) / original_size) * 100

    # Chuyển đổi kích thước tệp sang MB để dễ đọc
    original_size_mb = original_size / (1024 * 1024)
    compressed_size_mb = compressed_size / (1024 * 1024)

    print(f"Đã nén ảnh (không mất dữ liệu) và lưu tại: {output_file}")
    print(f"Thời gian nén: {compression_time:.2f} giây")
    print(f"Kích thước tệp trước khi nén: {original_size_mb:.2f} MB")
    print(f"Kích thước tệp sau khi nén: {compressed_size_mb:.2f} MB")
    print(f"Giảm dung lượng: {reduction_percentage:.2f}%")

# Ví dụ sử dụng
input_image = 'C:/anhnghiencuu/anhnghiencuu/multi_band4.tif'  # Đường dẫn đến ảnh gốc
output_image_lossless = 'C:/anhnghiencuu/anhnghiencuu/compressed_image_lossless.webp'  # Đường dẫn đến ảnh nén không mất dữ liệu

# Nén không mất dữ liệu
compress_to_webp_lossless(input_image, output_image_lossless)
