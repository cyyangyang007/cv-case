from ultralytics import YOLO

# 独立验证
model = YOLO("runs/detect/train/weights/best.pt")
# 如果不设置数据，它将使用model.pt中的数据集相关yaml文件。
metrics = model.val()
# 也可以设置自已想要的验证数据
# metrics = model.val(data='coco128.yaml')

print(metrics.box.map)    # map50-95
print(metrics.box.map50)  # map50
print(metrics.box.map75)  # map75
print(metrics.box.maps)  # a list contains map50-95 of each category