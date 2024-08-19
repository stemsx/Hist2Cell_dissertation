import os
import pandas as pd
from PIL import Image

class CropToSpot:
    def __init__(self, spot_radius):
        self.spot_radius = spot_radius

    def __call__(self, img, spot_coords):
        crops = []
        for spot_id, (x, y) in spot_coords.items():
            left = x - self.spot_radius
            top = y - self.spot_radius
            right = x + self.spot_radius
            bottom = y + self.spot_radius
            crop = img.crop((left, top, right, bottom))
            crops.append((spot_id, crop))
        return crops

def read_csv_data(csv_path):
    try:
        df = pd.read_csv(csv_path)
        spot_coords_dict = {row['spot_id']: (row['x'], row['y']) for _, row in df.iterrows()}
        return spot_coords_dict
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def main():
    csv_path = 'tissue_positions_list.csv'  # 替换为实际的 CSV 文件路径
    img_path = "aligned_fiducials.jpg"  # 替换为实际图像路径
    output_dir = "../patch/"  # 输出目录

    # 读取 CSV 文件数据
    spot_coords_dict = read_csv_data(csv_path)
    if spot_coords_dict is None:
        print("Failed to read CSV data.")
        return

    # 实例化裁剪类
    transform = CropToSpot(spot_radius=112)

    # 加载示例图像
    try:
        img = Image.open(img_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # 裁剪图像为多个 spot 的部分
    crops = transform(img, spot_coords_dict)

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 保存每个裁剪部分为单独的图像
    for spot_id, crop in crops:
        crop.save(os.path.join(output_dir, f"crop_{spot_id}.jpg"))

    print(f"{len(crops)} crops saved in '{output_dir}'")

if __name__ == "__main__":
    main()
