import os
import time
from osgeo import gdal

def decompress_tiff(input_file, output_file):
    # Mở tệp GeoTIFF đã nén
    dataset = gdal.Open(input_file)

    # Kiểm tra xem tệp có mở thành công không
    if dataset is None:
        print("Không thể mở tệp GeoTIFF.")
        return

    # Lấy dung lượng tệp trước khi giải nén
    compressed_size = os.path.getsize(input_file)

    # Tạo tùy chọn cấu hình để không áp dụng nén (COMPRESS=NONE)
    options = ['COMPRESS=NONE']

    # Bắt đầu tính thời gian
    start_time = time.time()

    # Giải nén và lưu tệp GeoTIFF mới
    gdal.Translate(output_file, dataset, format='GTiff', creationOptions=options)

    # Tính toán thời gian giải nén
    end_time = time.time()
    decompression_time = end_time - start_time

    # Giải phóng bộ nhớ
    dataset = None

    # Lấy dung lượng tệp sau khi giải nén
    uncompressed_size = os.path.getsize(output_file)

    # Tính phần trăm dung lượng tăng
    increase_percentage = ((uncompressed_size - compressed_size) / compressed_size) * 100

    # Chuyển đổi kích thước tệp sang MB để dễ đọc
    compressed_size_mb = compressed_size / (1024 * 1024)
    uncompressed_size_mb = uncompressed_size / (1024 * 1024)

    # In thông tin ra màn hình
    print(f"Đã giải nén tệp GeoTIFF và lưu tại: {output_file}")
    print(f"Thời gian giải nén: {decompression_time:.2f} giây")
    print(f"Kích thước tệp trước khi giải nén: {compressed_size_mb:.2f} MB")
    print(f"Kích thước tệp sau khi giải nén: {uncompressed_size_mb:.2f} MB")
    print(f"Tăng dung lượng: {increase_percentage:.2f}%")

# Ví dụ sử dụng
input_image = 'C:/anhnghiencuu/anhnghiencuu/compressed_image_lzw.tif'  # Đường dẫn đến tệp nén
output_image = 'C:/anhnghiencuu/anhnghiencuu/uncompressed_image.tif'  # Đường dẫn đến tệp đã giải nén

decompress_tiff(input_image, output_image)
