# -*- coding: UTF-8 -*-
# Created on 2024/3/31-22:06
import os

import PIL.Image
import cv2
import matplotlib.pyplot as plt
import numpy as np


def new_txt():
    ttxt = r"D:\Pycharm_Projects\UNet\unet-tf2_HV\Medical_Datasets\ImageSets\Segmentation\train.txt"


    ip = r'D:\Pycharm_Projects\UNet\unet-tf2_HV\Medical_Datasets\Images'

    import os

    with open(ttxt, 'w', encoding='u8') as F:
        for f in os.listdir(ip):
            print(f.split('.')[0], file=F)


def suit_label():
    lbs = os.listdir('Labels')
    for f in lbs:
        new_file_name = f.replace('_HGE_Seg', '').replace('jpg', 'png')
        f = os.path.join('Labels', f)
        new_file_name = os.path.join('Labels', new_file_name)

        os.rename(f, new_file_name)

        print(new_file_name)


if __name__ == '__main__':
    import cv2
    import numpy as np
    import os

    # 定义图片所在的目录
    directory = r"D:\Pycharm_Projects\UNet\unet-tf2_HV\Medical_Datasets\Labels"

    # 输出目录
    output_directory = r"D:\Pycharm_Projects\UNet\unet-tf2_HV\Medical_Datasets\Processed_Labels"
    os.makedirs(output_directory, exist_ok=True)

    # 遍历目录中的每个文件
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            # 构建完整的文件路径
            file_path = os.path.join(directory, filename)

            # 读取图片
            img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

            # 检查图片是否成功读取
            if img is not None:
                # 将所有非零像素转换为1
                img_binary = np.where(img > 0, 1, 0).astype(np.uint8)

                # 构建输出文件路径
                output_path = os.path.join(output_directory, filename)

                # 保存处理后的图片
                cv2.imwrite(output_path, img_binary)  # 乘以255将1转换为255，以符合二值图像的一般表示
            else:
                print(f"图片 {filename} 无法读取。")

    print("处理完成。")
