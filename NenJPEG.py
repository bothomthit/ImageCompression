import os
import time
from osgeo import gdal

# Đường dẫn tệp đầu vào và đầu ra
input_file = "C:/anhnghiencuu/anhnghiencuu/multi_band.tif"
output_file = "C:/anhnghiencuu/anhnghiencuu/compressed_image.jp2"

# Mở tệp ảnh đầu vào
dataset = gdal.Open(input_file)

# Kiểm tra xem tệp đã mở thành công
if dataset is None:
    print("Không thể mở tệp ảnh.")
else:
    # Lấy kích thước tệp trước khi nén
    original_size = os.path.getsize(input_file)

    # Lưu dưới định dạng JPEG 2000
    options = ['QUALITY=75']  # Điều chỉnh giá trị chất lượng (từ 1 đến 100)

    # Bắt đầu tính thời gian
    start_time = time.time()

    # Nén và lưu tệp
    gdal.Translate(output_file, dataset, format='JP2OpenJPEG', creationOptions=options)

    # Đóng dataset
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

    print("Nén ảnh thành công!")
    print(f"Thời gian nén: {compression_time:.2f} giây")
    print(f"Kích thước tệp trước khi nén: {original_size_mb:.2f} MB")
    print(f"Kích thước tệp sau khi nén: {compressed_size_mb:.2f} MB")
    print(f"Giảm dung lượng: {reduction_percentage:.2f}%")
