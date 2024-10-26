import os
import time
from osgeo import gdal

def compress_tiff_with_lzw(input_file, output_file):
    # Mở tệp GeoTIFF gốc
    dataset = gdal.Open(input_file)

    # Kiểm tra xem tệp có mở thành công không
    if dataset is None:
        print("Không thể mở tệp GeoTIFF.")
        return

    # Lấy dung lượng tệp trước khi nén
    original_size = os.path.getsize(input_file)

    # Tạo tùy chọn cấu hình cho nén LZW
    options = ['COMPRESS=LZW']

    # Bắt đầu tính thời gian
    start_time = time.time()

    # Nén và lưu tệp GeoTIFF mới
    gdal.Translate(output_file, dataset, format='GTiff', creationOptions=options)

    # Tính toán thời gian nén
    end_time = time.time()
    compression_time = end_time - start_time

    # Giải phóng bộ nhớ
    dataset = None

    # Lấy dung lượng tệp sau khi nén
    compressed_size = os.path.getsize(output_file)

    # Tính phần trăm dung lượng giảm
    reduction_percentage = ((original_size - compressed_size) / original_size) * 100

    # Chuyển đổi kích thước tệp sang MB để dễ đọc
    original_size_mb = original_size / (1024 * 1024)
    compressed_size_mb = compressed_size / (1024 * 1024)

    # In thông tin ra màn hình
    print(f"Đã nén tệp GeoTIFF và lưu tại: {output_file}")
    print(f"Thời gian nén: {compression_time:.2f} giây")
    print(f"Kích thước tệp trước khi nén: {original_size_mb:.2f} MB")
    print(f"Kích thước tệp sau khi nén: {compressed_size_mb:.2f} MB")
    print(f"Giảm dung lượng: {reduction_percentage:.2f}%")

# Ví dụ sử dụng
input_image = 'C:/anhnghiencuu/anhnghiencuu/multi_band.tif'  # Đường dẫn đến tệp gốc
output_image = 'C:/anhnghiencuu/anhnghiencuu/compressed_image_lzw.tif'  # Đường dẫn đến tệp đã nén

compress_tiff_with_lzw(input_image, output_image)
