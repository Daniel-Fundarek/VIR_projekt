from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
# model = YOLO('yolov8s.pt')
model = YOLO('yolov8s.pt')


# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data='/home/dfundo/workspace/VIR_projekt/labeled_images_rotated_resized/data.yaml', cfg='/home/dfundo/workspace/VIR_projekt/args.yaml')
