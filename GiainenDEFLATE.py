from osgeo import gdal
import os
import time

# Đường dẫn đến tệp GeoTIFF nén
compressed_file = "C:/anhnghiencuu/anhnghiencuu/compressed_multi_band.tif"

# Đường dẫn lưu file giải nén (ảnh gốc)
uncompressed_file = "C:/anhnghiencuu/anhnghiencuu/uncompressed_multi_band.tif"

# Kiểm tra dung lượng tệp trước khi giải nén
compressed_size = os.path.getsize(compressed_file)
print(f"Dung lượng trước khi giải nén: {compressed_size / (1024 * 1024):.2f} MB")

# Mở tệp nén bằng GDAL
dataset = gdal.Open(compressed_file)

# Kiểm tra xem tệp có mở thành công không
if dataset is None:
    print(f"Không thể mở tệp: {compressed_file}")
else:
    # Bắt đầu đo thời gian giải nén
    start_time = time.time()

    # Giải nén (tạo bản sao không có nén)
    driver = gdal.GetDriverByName("GTiff")
    uncompressed_dataset = driver.CreateCopy(uncompressed_file, dataset, options=["COMPRESS=NONE"])

    # Đóng file
    uncompressed_dataset = None
    dataset = None

    # Kết thúc đo thời gian giải nén
    end_time = time.time()
    decompression_time = end_time - start_time

    # Kiểm tra dung lượng tệp sau khi giải nén
    uncompressed_size = os.path.getsize(uncompressed_file)
    print(f"Dung lượng sau khi giải nén: {uncompressed_size / (1024 * 1024):.2f} MB")

    # Tính toán phần trăm dung lượng tăng lên sau khi giải nén
    size_increase_percentage = ((uncompressed_size - compressed_size) / compressed_size) * 100
    print(f"Thời gian giải nén: {decompression_time:.2f} giây")
    print(f"Tăng dung lượng: {size_increase_percentage:.2f}%")
  