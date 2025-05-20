
from ultralytics import YOLO
import cv2

traducao_classes = {
    0: "Pulgão",
    1: "Lagarta (armyworm)",
    2: "Lagarta",
    4: "Lagarta (cutworm)",
    10: "Percevejo"
}

model = YOLO("runs/detect/train4/weights/best.pt")

results = model.predict(source="teste2.webp", conf=0.1, save=False)

img = cv2.imread("teste2.webp")

for r in results:
    boxes = r.boxes
    for box in boxes:
        cls_id = int(box.cls[0])
        nome = traducao_classes.get(cls_id, f"Classe {cls_id}")
        conf = float(box.conf[0])
        xyxy = box.xyxy[0].tolist()
        x1, y1, x2, y2 = map(int, xyxy)
        label = f"{nome} ({conf:.2f})"
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow("Resultado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
