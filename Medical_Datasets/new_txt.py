# -*- coding: UTF-8 -*-
# Created on 2024/3/31-22:06

ttxt = r"D:\Pycharm_Projects\UNet\unet-tf2_HV\Medical_Datasets\ImageSets\Segmentation\train.txt"


ip = r'D:\Pycharm_Projects\UNet\unet-tf2_HV\Medical_Datasets\Images'

import os

with open(ttxt, 'w', encoding='u8') as F:
    for f in os.listdir(ip):
        print(f.split('.')[0], file=F)


