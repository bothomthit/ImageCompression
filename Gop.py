from osgeo import gdal
import numpy as np

# # Đường dẫn đến các tệp band
band_files = [
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B1.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B3.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B4.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B5.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B6.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B7.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B8.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B9.tif",
    "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B2.tif"
]
# band_files = [
#     "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B1.tif",
#     "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B2.tif",
#     "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B3.tif",
#     "C:/anhnghiencuu/anhnghiencuu/LO08_L1TP_125052_20191221_20200924_02_T1_B4.tif"
# ]
# Đường dẫn lưu file GeoTIFF gộp
output_combined_file = "C:/anhnghiencuu/anhnghiencuu/multi_band.tif"
# output_combined_file = "C:/anhnghiencuu/anhnghiencuu/multi_band4.tif"
# Tạo tệp GeoTIFF gộp
driver = gdal.GetDriverByName("GTiff")

# Xác định kích thước lớn nhất
max_width = 0
max_height = 0
for band_file in band_files:
    band_dataset = gdal.Open(band_file)
    if band_dataset:
        band_width = band_dataset.RasterXSize
        band_height = band_dataset.RasterYSize
        if band_width > max_width:
            max_width = band_width
        if band_height > max_height:
            max_height = band_height
        band_dataset = None  # Đóng band dataset

# Tạo tệp GeoTIFF gộp với kích thước lớn nhất
combined_dataset = driver.Create(output_combined_file,
                                 max_width,
                                 max_height,
                                 len(band_files),
                                 gdal.GDT_Byte)  # Chọn kiểu dữ liệu phù hợp

# Thêm từng band vào tệp gộp
for i, band_file in enumerate(band_files):
    band_dataset = gdal.Open(band_file)
    if band_dataset is not None:
        # Lấy kích thước của band hiện tại
        band_width = band_dataset.RasterXSize
        band_height = band_dataset.RasterYSize

        print(f"Kích thước band {i + 1} ({band_file}): {band_width} x {band_height}")

        # Đọc dữ liệu từ band hiện tại
        band_data = band_dataset.GetRasterBand(1).ReadAsArray()

        # Tạo mảng trống cho band hiện tại có kích thước lớn nhất
        array = np.zeros((max_height, max_width), dtype=np.uint8)

        # Gán dữ liệu vào mảng trống, sử dụng slice để chỉ định vị trí
        array[:band_height, :band_width] = band_data

        # Ghi mảng vào band của tệp gộp
        combined_dataset.GetRasterBand(i + 1).WriteArray(array)
        band_dataset = None  # Đóng band dataset
    else:
        print(f"Không thể mở tệp band: {band_file}")

# Đóng tệp gộp
combined_dataset = None

print(f"Đã gộp và lưu các band vào: {output_combined_file}")
