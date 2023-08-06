"""
See more detail in official doc: 
https://docs.ultralytics.com/modes/val/
"""

from ultralytics import YOLO

# Load a model
# model = YOLO('yolov8n.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model
model = YOLO("runs/detect/train/weights/best.pt") # Load the best weight


# Validate the model

metrics = model.val() # It'll automatically evaluate the data you trained.
# metrics = model.val(data='coco128.yaml') # Or set the data you want to evaluate

print(metrics.box.map)    # map50-95
print(metrics.box.map50)  # map50
print(metrics.box.map75)  # map75
print(metrics.box.maps)  # a list contains map50-95 of each category