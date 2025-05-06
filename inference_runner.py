import os
import sys
import time
import json
import cv2

# Patch PosixPath for Windows
import pathlib
_temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

import torch

# ✅ Setup paths
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")
OUTPUT_JSON = os.path.join(BASE_DIR, "inference_output.json")
YOLOV5_PATH = os.path.join(BASE_DIR, "yolov5")

# Add YOLOv5 path
sys.path.insert(0, YOLOV5_PATH)

# Import YOLOv5 internals
from models.common import DetectMultiBackend
from utils.general import non_max_suppression, scale_boxes
from utils.torch_utils import select_device
from utils.augmentations import letterbox

# Device and model
device = select_device("")
model = torch.load(MODEL_PATH, map_location=device)["model"].float().fuse().eval()
names = model.names
print(f"✅ Model loaded: {MODEL_PATH}")
print("🔍 Classes:", names)

# Restore original
pathlib.PosixPath = _temp

# Webcam fallback logic
cap = None
for index in [0, 1, 2]:
    for backend in [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_V4L2]:
        print(f"🔍 Trying index {index} with backend {backend}...")
        test_cap = cv2.VideoCapture(index, backend)
        if test_cap.isOpened():
            print(f"✅ Webcam opened with index {index} and backend: {backend}")
            cap = test_cap
            break
        else:
            print(f"❌ Failed to open webcam with index {index} and backend {backend}")
    if cap:
        break

if not cap or not cap.isOpened():
    print("❌ Webcam not accessible with any backend or index.")
    exit()

print("✅ Webcam ready.")

def preprocess(frame):
    img = letterbox(frame, new_shape=(640, 640))[0]
    img = img[:, :, ::-1].copy().transpose(2, 0, 1)
    img = torch.from_numpy(img).to(device)
    img = img.float() / 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    return img

def estimate_distance(bbox):
    width = bbox[2] - bbox[0]
    return f"{round(200 - width, 1)}m"

last_write_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame from webcam.")
        break

    img_tensor = preprocess(frame)
    pred = model(img_tensor)[0]
    pred = non_max_suppression(pred, 0.25, 0.45)

    detected_objects = []

    for det in pred:
        if len(det):
            det[:, :4] = scale_boxes(img_tensor.shape[2:], det[:, :4], frame.shape).round()

            for *xyxy, conf, cls in det:
                if conf < 0.6:
                    continue

                cls_id = int(cls.item())
                label = names[cls_id]
                bbox = [float(x.item()) for x in xyxy]
                distance = estimate_distance(bbox)

                print(f"🧠 Detected: {label} at {distance} ({conf:.2f})")

                # ✅ Draw red bounding box
                cv2.rectangle(
                    frame,
                    (int(xyxy[0]), int(xyxy[1])),
                    (int(xyxy[2]), int(xyxy[3])),
                    (0, 0, 255), 2
                )
                cv2.putText(
                    frame,
                    f'{label} {conf:.2f}',
                    (int(xyxy[0]), int(xyxy[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255), 2
                )

                detected_objects.append({
                    "class": label,
                    "distance": distance
                })

    # Save detections every 3s
    if time.time() - last_write_time > 3:
        output = {
            "weather": "Clear",
            "objects": detected_objects
        }
        with open(OUTPUT_JSON, "w") as f:
            json.dump(output, f, indent=2)
        print("📤 inference_output.json updated.\n")
        last_write_time = time.time()

    cv2.imshow("YOLOv5 Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
