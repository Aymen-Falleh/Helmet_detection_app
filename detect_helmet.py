# Run prediction on all test images
from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

results = model.predict(
    source='dataset/test/images',    # relative path to test images folder
    conf=0.25,               # confidence threshold
    save=True,               # save images with bounding boxes
    save_txt=False,          # disable saving .txt files if not needed
    project='results',       # save results in 'results' folder locally
    name='inference_on_test_set',  
    imgsz=640
)
