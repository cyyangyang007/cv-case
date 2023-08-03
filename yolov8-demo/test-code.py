# -*- coding: utf-8 -*-
# @Author: Caoyang
# @Email: 970659981@qq.com
# @Last Modified time: 2023-08-02 23:05:07
# @Description:

from pathlib import Path
# Path将文件或者文件夹路径（str）转换为Path对象， 可以实现不同OS路径连接符问题不同、以及对该路径的其他操作，如判断是否为文件、文件夹，根据路径创建创建文件夹（包括是否递归创建缺少的文件夹）等。
# __file__是Python中内置的变量,它表示当前文件的文件名。
# path.resolve() 解析为绝对路径
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLO
print(ROOT)