import os
import time
from osgeo import gdal

def decompress_webp_lossy_to_tiff(input_file, output_file):
    # Mở tệp WebP đã nén
    dataset = gdal.Open(input_file)

    # Kiểm tra xem tệp đã mở thành công chưa
    if dataset is None:
        print("Không thể mở tệp WebP.")
        return

    # Lấy kích thước tệp WebP trước khi giải nén
    compressed_size = os.path.getsize(input_file)

    # Bắt đầu tính thời gian giải nén
    start_time = time.time()

    # Giải nén WebP và lưu dưới định dạng GeoTIFF (không nén thêm)
    gdal.Translate(output_file, dataset, format='GTiff')

    # Giải phóng bộ nhớ
    dataset = None

    # Tính toán thời gian giải nén
    end_time = time.time()
    decompression_time = end_time - start_time

    # Lấy kích thước tệp sau khi giải nén
    uncompressed_size = os.path.getsize(output_file)

    # Tính phần trăm dung lượng tăng
    increase_percentage = ((uncompressed_size - compressed_size) / compressed_size) * 100

    # Chuyển đổi kích thước tệp sang MB để dễ đọc
    compressed_size_mb = compressed_size / (1024 * 1024)
    uncompressed_size_mb = uncompressed_size / (1024 * 1024)

    print(f"Đã giải nén tệp WebP (có mất dữ liệu) và lưu tại: {output_file}")
    print(f"Thời gian giải nén: {decompression_time:.2f} giây")
    print(f"Kích thước tệp WebP: {compressed_size_mb:.2f} MB")
    print(f"Kích thước tệp GeoTIFF sau khi giải nén: {uncompressed_size_mb:.2f} MB")
    print(f"Tăng dung lượng: {increase_percentage:.2f}%")

# Ví dụ sử dụng
input_image = 'C:/anhnghiencuu/anhnghiencuu/compressed_image_lossy.webp'  # Đường dẫn đến tệp WebP nén (mất dữ liệu)
output_image = 'C:/anhnghiencuu/anhnghiencuu/decompressed_image_lossy.tif'  # Đường dẫn đến tệp GeoTIFF sau giải nén

# Giải nén WebP về GeoTIFF
decompress_webp_lossy_to_tiff(input_image, output_image)
