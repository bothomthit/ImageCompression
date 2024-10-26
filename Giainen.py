from osgeo import gdal
import os

# Đường dẫn đến tệp GeoTIFF nén
compressed_file = "C:/anhnghiencuu/anhnghiencuu/compressed_multi_band.tif"

# Mở tệp GeoTIFF nén
dataset = gdal.Open(compressed_file)

# Kiểm tra thông tin tệp
if dataset is not None:
    print("Tệp đã được mở thành công!")

    # Lấy thông tin cơ bản về tệp
    print(f"Số lượng băng (bands): {dataset.RasterCount}")
    print(f"Kích thước hình ảnh: {dataset.RasterXSize} x {dataset.RasterYSize}")
    print(f"Định dạng tệp: {dataset.GetDriver().ShortName}")

    # Lấy dung lượng tệp
    file_size = os.path.getsize(compressed_file)
    print(f"Dung lượng tệp nén: {file_size / (1024 * 1024):.2f} MB")

    # Bạn có thể truy cập dữ liệu băng (band) nếu cần
    band = dataset.GetRasterBand(1)  # Lấy băng đầu tiên
    print(f"Giá trị tối đa: {band.GetMaximum()}")
    print(f"Giá trị tối thiểu: {band.GetMinimum()}")
    
    # Đóng tệp sau khi hoàn tất
    dataset = None
else:
    print("Không thể mở tệp.")
