# -*- coding: utf-8 -*-
# @Author: Caoyang
# @Email: 970659981@qq.com
# @Last Modified time: 2023-07-27 23:06:18
# @Description: 找到标注的类别，生成classes保存到txt

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir
from os.path import join

include_difficult = True
XML_DIR = 'labels'  # 原始目录，保存xml
classes = [] # 可以填写部分已知的类，程序自动补全


print("Searching...")
print("Considering difficult labels?",include_difficult,"\n")
list=os.listdir(XML_DIR)
for i in range(0,len(list)):
    try:
        path = os.path.join(XML_DIR,list[i])
        # 读取xml
        with open(path, "r", encoding='UTF-8') as in_file:
            tree=ET.parse(in_file)
            root = tree.getroot()
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if include_difficult == True:
                if cls not in classes:
                    classes.append(cls)
                    print("====== Find a new class name:", cls)
            else:
                if cls not in classes and int(difficult) == 0:
                    classes.append(cls)
                    print("====== Find a new class name:", cls)
            with open("classes.txt","w") as f:
                f.write(str(classes))
    except Exception as e:
        print("Exception: ", e)


if len(classes) > 1:
    print("\nDetect "+str(len(classes))+" classes ：",classes)
elif len(classes) == 1:
    print("\nDetect 1 class：",classes)
else:
    print("Not a single one class was detected")


