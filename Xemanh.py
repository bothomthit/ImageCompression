from osgeo import gdal
import numpy as np
from PIL import Image

def display_image_with_gdal(image_path):
    try:
        # Mở ảnh sử dụng GDAL
        dataset = gdal.Open(image_path)

        if dataset is None:
            print(f"Không thể mở ảnh {image_path}.")
            return

        print(f"Đã mở ảnh: {image_path}")
        print(f"Số băng: {dataset.RasterCount}")
        print(f"Kích thước: {dataset.RasterXSize} x {dataset.RasterYSize}")

        # Lấy dữ liệu từ băng đầu tiên
        band = dataset.GetRasterBand(1)
        data = band.ReadAsArray()

        # Chuyển đổi dữ liệu thành ảnh
        img = Image.fromarray(data)

        # Hiển thị ảnh
        img.show()

        # Giải phóng bộ nhớ
        dataset = None
    except Exception as e:
        print(f"Không thể mở ảnh {image_path}: {e}")

# Gọi hàm cho từng ảnh
display_image_with_gdal('C:/anhnghiencuu/anhnghiencuu/compressed_multi_band.tif')            # Ảnh nén bằng DEFLATE
display_image_with_gdal('C:/anhnghiencuu/anhnghiencuu/compressed_image_lossless.webp')       # Ảnh nén bằng WebP (không mất dữ liệu)
display_image_with_gdal('C:/anhnghiencuu/anhnghiencuu/compressed_image_lossy.webp')          # Ảnh nén bằng WebP (mất dữ liệu)
display_image_with_gdal('C:/anhnghiencuu/anhnghiencuu/compressed_image.jp2')                 # Ảnh nén bằng JPEG 2000
display_image_with_gdal('C:/anhnghiencuu/anhnghiencuu/compressed_image_lzw.tif')             # Ảnh nén bằng LZW
