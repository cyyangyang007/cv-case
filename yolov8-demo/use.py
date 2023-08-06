"""
Quickly implemention
Users can load a model, train it, evaluate its performance on a validation set, 
and even export it to ONNX format with just a few lines of code.
See more usage in https://docs.ultralytics.com/usage/python/
"""

from ultralytics import YOLO

# Load a model
# model = YOLO('cfg/yolov8n.yaml').load('./weights/yolov8n.pt')  # build from YAML and transfer weights
model = YOLO('cfg/yolov8n.yaml')  # build a new model from scratch

# Use the model
model.train(data='data/data.yaml', epochs=5, batch=-1, imgsz=640, workers=0) # windows下workers设置为0

# evaluate model performance on the validation set
metrics = model.val() 
# print(metrics.box.map)    # map50-95
# print(metrics.box.map50)  # map50
# print(metrics.box.map75)  # map75
# print(metrics.box.maps)  # a list contains map50-95 of each category

# predict on an image
results = model(source="data/test/images", save=True)

# Export the model to ONNX format
success = model.export(format='onnx')