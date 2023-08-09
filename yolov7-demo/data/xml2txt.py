# -*- coding: utf-8 -*-
# @Author: Caoyang
# @Email: 970659981@qq.
# @Last Modified time: 2023-07-27 16:26:08
# @Description: yolo检测使用的标注文件转换，v5、v7、v8可用 


import xml.etree.ElementTree as ET
# import pickle
import os
from os import listdir
from os.path import join

# 需要修改的参数
XML_DIR = 'labels'  # 原始目录，保存xml
TXT_DIR = "txt"  # 新目录，保存txt
classes = ["cat"] # 参与训练的类，可选classes的子集
include_difficult = True # 是否训练标注的difficult目标
remove_xml = False # 是否删除xml文件

def convert(size, box):
    """
    Function: 标注框数值归一化（原数值除以宽和高）
    === Arguments ===
    size：(w,h),表示图像宽高的二元组
    box：(xmin,xmax,ymin,ymax) 中心点坐标，左上角和左下角

    === Return ===
    (x,y,w,h)：返回目标边框的中心点和宽高相对于图像宽高的比例
    """
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    if w >= 1:
        w = 0.99
    if h >= 1:
        h = 0.99
    return (x, y, w, h)

 
def convert_annotation(xmlpath, xmlname):
    """
    Function: 读取并解析xml的标注信息，转写入txt
    === Arguments ===
    xmlpath：xml文件的完整路径（目录+名称）
    xmlname：xml文件的名称

    === Return ===
    无返回值
    """
    # 读取xml
    with open(xmlpath, "r", encoding='UTF-8') as in_file:
        tree=ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        # 赋值w,h：宽和高
        w = int(size.find('width').text)
        h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # 排除非特定类别和difficult项
        if include_difficult == False:
            if cls not in classes or int(difficult)==1:
                print("------ Skiping:"+xmlname, "class:"+cls, "difficult:"+difficult)
                continue
        else:
            if cls not in classes:
                print("------ Skiping:"+xmlname, "class:"+cls, "Difficult:"+difficult)
                continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        # 赋值b： (xmin,xmax,ymin,ymax) 表示左上角和右下角坐标(第四象限，原点在左上角)
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), \
            float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        # 写入txt
        txtname = xmlname[:-4] + '.txt'
        txtpath = os.path.join(TXT_DIR,txtname)
        with open(txtpath, "w+" ,encoding='UTF-8') as out_file: 
            # out_file.truncate()
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        print(f'file {list[i]} convert success.')
 
if __name__ == "__main__":
    # if not os.path.exists(TXT_DIR):
    #     os.makedirs(TXT_DIR)
    os.makedirs(TXT_DIR, exist_ok=True)
     # 数据标签

    error_file_list = []
    list=os.listdir(XML_DIR)
    for i in range(0,len(list)):
        try:
            path = os.path.join(XML_DIR,list[i])
            if ('.xml' in path) or ('.XML' in path):
                convert_annotation(path, list[i])
                
            else:
                print(f'file {list[i]} is not xml format.')
            if remove_xml:
                os.remove(path) # 删除xml文件
        except Exception as e:
            print(f'file {list[i]} convert error.')
            print(f'error message:\n{e}')
            error_file_list.append(list[i])
    print(f'this file convert failure: {error_file_list}')
    print(f'Dataset Classes:{classes}')