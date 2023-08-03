from ultralytics import YOLO # 导入ultralytics.models.yolo中model.py定义的YOLO类
from PIL import Image
import cv2


# 用训练得到的权重替换，文件选runs/detect/train[数字最大的]/weights/last.pt
model = YOLO("runs/detect/train4/weights/best.pt") 

# Predict with the model
results = model(source="data/test/images",save=True) 


# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcamresults = model.predict(source="0")

# 用摄像头
# results = model.predict(source="0")

# from dir
# results = model.predict(source="folder",show=True) # Display preds. Accepts all YOLO predict argument

# from PIL
# im1 = Image.open("data/test/images/4.jpg") # 找一个
# results = model.predict(source=im1, save=True) # save plotted images

# from ndarray
# im2 = cv2.imread("test.jpg")
# results = model.predict(source=im2,save=True,save_txt=True) # save predictions as labels
# # from list of PIL/ndancay
# results = model. predict(source=[im1, im2])