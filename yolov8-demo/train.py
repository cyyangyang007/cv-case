"""
See more detail in official doc: 
https://docs.ultralytics.com/modes/train/
"""

from ultralytics import YOLO

# Load a model
model = YOLO('cfg/yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
model.train(data='data/data.yaml', epochs=100, imgsz=640, workers=0)