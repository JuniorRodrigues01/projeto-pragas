from ultralytics import YOLO


model = YOLO("yolov8n.pt")


model.train(data="C:/Users/junio/Desktop/projeto-pragas/dataset_yolo/data.yaml", epochs=50, imgsz=640)


