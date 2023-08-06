"""
See more detail in official doc: 
https://docs.ultralytics.com/modes/predict/
"""


from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train/weights/best.pt") # Load the best weight

# Predict with the model
results = model(source="data/test/images",save=True) # from dir

# Run batched inference on a list of images
# results = model(['im1.jpg', 'im2.jpg']) # return a list of Results objects
# results = model(['im1.jpg', 'im2.jpg'], stream=True)  # return a generator of Results objects

# Process results
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs




