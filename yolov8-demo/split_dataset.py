# -*- coding: utf-8 -*-
# @Author: Caoyang
# @Email: 970659981@qq.com
# @Last Modified time: 2023-07-22 10:34:12
# @Description: 把images和labels中的文件划分成train、val、test三个数据集
#               拆分后的数据直接移动到新文件夹，使用前保留一份原数据集拷贝



import os
import random
from tqdm import tqdm


# 指定保存图片和标注文件的根目录和文件夹
ROOT_DIR = "./data/"
IMAGE_FOLDER = "images"
LABEL_FOLDER = "labels"


if __name__ == '__main__':
    image_dir = f"{ROOT_DIR}{IMAGE_FOLDER}"
    label_dir = f"{ROOT_DIR}{LABEL_FOLDER}"
    valid_images = []
    valid_labels = []
    sets = ["train", "val", "test"]
    for i in sets:
        os.makedirs(ROOT_DIR+i+"/", exist_ok=True)
        os.makedirs(ROOT_DIR+i+"/"+IMAGE_FOLDER, exist_ok=True)
        os.makedirs(ROOT_DIR+i+"/"+LABEL_FOLDER, exist_ok=True)


    # 遍历images匹配对应的txt文件名
    for image_name in os.listdir(image_dir):
        # 获取图片的完整路径
        image_path = os.path.join(image_dir, image_name)
        # print(image_path)
        # 替换扩展名
        ext = os.path.splitext(image_name)[-1]
        label_name = image_name.replace(ext, ".txt")
        # 获取对应 label 的完整路径
        label_path = os.path.join(label_dir, label_name)
        print(label_path)
        # 删掉没有标注的图片
        if not os.path.exists(label_path):
            os.remove(image_path)
            print("Delete -- picture unlabeld：", image_path)
        else:
            # 将图片路径添加到列表中
            valid_images.append(image_path)
            # 将label路径添加到列表中
            valid_labels.append(label_path)
            # print("valid:", image_path, label_path)


    # 遍历每个有效图片路径
    for i in tqdm(range(len(valid_images))):
        image_path = valid_images[i]
        label_path = valid_labels[i]
        # 随机生成一个概率
        r = random.random()
        # 判断图片应该移动到哪个文件夹
        # train：valid：test = 7:3:1
        if r < 0.1:
            # 移动到 test 文件夹
            destination = f"{ROOT_DIR}test"
        elif r < 0.2:
            # 移动到 valid 文件夹
            destination = f"{ROOT_DIR}val"
        else:
            # 移动到 train 文件夹
            destination = f"{ROOT_DIR}train"



        # 生成目标文件夹中图片的新路径
        image_destination_path = os.path.join(destination, IMAGE_FOLDER, os.path.basename(image_path))
        # 移动图片到目标文件夹
        os.rename(image_path, image_destination_path)
        # 生成目标文件夹中 label 的新路径
        label_destination_path = os.path.join(destination, LABEL_FOLDER, os.path.basename(label_path))
        # 移动 label 到目标文件夹
        os.rename(label_path, label_destination_path)

    #输出有效列表
    print("valid images:", len(valid_images))
    print("valid labels:", len(valid_labels))
