from ultralytics import YOLO

# Load a model
# model = YOLO('./data/fall.yaml')  # build a new model from YAML
# model = YOLO('./fall.yaml').load('yolov8n.pt')  # build from YAML and transfer weights
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model
model.train(data='./data/class.yaml', epochs=5, batch=-1, imgsz=640, workers=0) # windows下workers设置为0