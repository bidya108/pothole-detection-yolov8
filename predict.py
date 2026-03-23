from ultralytics import YOLO

model = YOLO("runs/detect/pothole_best/weights/best.pt")

model.predict(
    source="dataset/test/images",
    save=True,
    conf=0.25
)