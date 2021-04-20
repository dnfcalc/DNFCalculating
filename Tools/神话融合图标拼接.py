# Gif：导出图标所在
# Icon：需要合成的图标
# Top：特效所在文件夹，从1开始，后缀png
# Temp：临时文件夹
# 注意：ICON需要和TOP中的宽度、高度、位深度相同

from skimage import io
import shutil
import imageio
import os
import math
import numpy as np

# 线性减淡


def Linear_dodge(img_1, img_2):
    img = img_1 + img_2
    mask_2 = img > 1
    img = img * (1 - mask_2) + mask_2
    return img


def compose_gif(img_paths, fileName):
    gif_images = []
    for path in img_paths:
        gif_images.append(imageio.imread(path))
    # 间隔100毫秒
    imageio.mimsave("Gif/" + fileName[:-4] + ".gif", gif_images, duration=0.1)


if not os.path.exists("Temp"):
    os.mkdir("Temp")

Top_List = os.listdir("Top/")

for file in os.listdir("Icon"):
    file_path = os.path.join("Icon/", file)
    if not os.path.isdir(file_path):
        img_2 = io.imread(file_path)
        img_2 = img_2 / 255.0
        img_paths = []
        for i in range(1, len(Top_List)):
            file_name = os.path.join("Top/", str(i) + '.png')
            img_1 = io.imread(file_name)
            img_1 = img_1 / 255.0
            img = Linear_dodge(img_1, img_2)
            io.imsave('Temp\\' + str(i) + '.png', img)
            img_paths.append('Temp\\' + str(i) + '.png')
        compose_gif(img_paths, file)
        shutil.rmtree('Temp')
        os.mkdir("Temp")
