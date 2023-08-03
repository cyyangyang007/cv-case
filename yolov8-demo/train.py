from ultralytics import YOLO

# Load a model
# model = YOLO('./data/fall.yaml')  # build a new model from YAML
# model = YOLO('./fall.yaml').load('yolov8n.pt')  # build from YAML and transfer weights
model = YOLO('./cfg/yolov8n.yaml')  # load a pretrained model (recommended for training)

# Train the model
model.train(data='data/data.yaml', epochs=5, batch=-1, imgsz=640, workers=0) # windows下workers设置为0
metrics = model.val() # val after train
print(metrics.box.map)    # map50-95
print(metrics.box.map50)  # map50
print(metrics.box.map75)  # map75
print(metrics.box.maps)  # a list contains map50-95 of each category