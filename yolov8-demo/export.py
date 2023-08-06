"""
See more detail in official doc: 
https://docs.ultralytics.com/modes/export/
"""


from ultralytics import YOLO

# Load a model
model = YOLO('path/to/best.pt')  # load a custom trained

# Export the model
model.export(format='onnx')