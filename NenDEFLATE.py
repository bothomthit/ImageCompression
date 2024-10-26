from osgeo import gdal
import os
import time

# Đường dẫn đến tệp GeoTIFF gộp
output_combined_file = "C:/anhnghiencuu/anhnghiencuu/multi_band.tif"

# Đường dẫn lưu file GeoTIFF nén
output_file = "C:/anhnghiencuu/anhnghiencuu/compressed_multi_band.tif"

# Kiểm tra dung lượng tệp trước khi nén
combined_size = os.path.getsize(output_combined_file)
print(f"Dung lượng trước khi nén: {combined_size / (1024 * 1024):.2f} MB")

# Mở tệp gộp bằng GDAL
dataset = gdal.Open(output_combined_file)

# Kiểm tra xem tệp có mở thành công không
if dataset is None:
    print(f"Không thể mở tệp: {output_combined_file}")
else:
    # Bắt đầu đo thời gian nén
    start_time = time.time()

    # Nén toàn bộ dữ liệu ảnh và nén bằng DEFLATE
    driver = gdal.GetDriverByName("GTiff")
    compressed_dataset = driver.CreateCopy(output_file, dataset, options=["COMPRESS=DEFLATE"])

    # Đóng file
    compressed_dataset = None
    dataset = None

    # Kết thúc đo thời gian nén
    end_time = time.time()
    compression_time = end_time - start_time

    # Kiểm tra dung lượng tệp sau khi nén
    output_size = os.path.getsize(output_file)
    print(f"Dung lượng sau khi nén: {output_size / (1024 * 1024):.2f} MB")

    # Tính toán phần trăm dung lượng giảm
    size_reduction_percentage = ((combined_size - output_size) / combined_size) * 100
    print(f"Thời gian nén: {compression_time:.2f} giây")
    print(f"Giảm dung lượng: {size_reduction_percentage:.2f}%")
