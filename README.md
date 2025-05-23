# 🎙️ Voice-Centric AI Assistant (YOLOv5 + Tkinter)

This project is a voice-enabled desktop assistant that uses a trained YOLOv5 model to:

* Detect objects (like people, cars, traffic signs) in real time from your webcam
* Announce detections using speech synthesis
* Show live detection logs in a GUI
* Provide JSON output for other systems

---

## 📦 Features

👉 Real-time object detection via YOLOv5
👉 Voice alerts using `pyttsx3`
👉 Visual display using `tkinter`
👉 JSON file output for integration

---

## 📍 UI Components

| Section         | Description                                      |
| --------------- | ------------------------------------------------ |
| Top Bar         | System status (e.g., Running)                    |
| Detection Panel | Text area showing real-time detections           |
| Voice Alerts    | Spoken feedback like “Car detected at 50 meters” |

---

## 📊 Installation

### Clone the Repo

```bash
git clone <your-repo-url>
cd voice_ui_app
```

### Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Add your YOLOv5 model

Place your `best.pt` model in the root directory.

---

## ▶️ Running the App

### 1. Start Webcam Detection

```bash
python inference_runner.py
```

This script:

* Loads the YOLOv5 model
* Opens your webcam
* Draws bounding boxes
* Outputs `inference_output.json`

### 2. Start the UI + Voice Assistant

```bash
python ui_main.py
```

This script:

* Displays the GUI
* Monitors `inference_output.json`
* Speaks context-aware alerts

---

## 🔍 File Structure

```
voice_ui_app/
├── inference_runner.py       # Runs YOLO model on webcam
├── ui_main.py                # GUI + voice interface
├── speech_engine.py          # Manages pyttsx3 voice thread
├── best.pt                   # Your trained YOLOv5 model
├── inference_output.json     # Shared output for detections
├── yolov5/                   # (Optional) YOLOv5 cloned repo
├── requirements.txt          # Required packages
└── README.md                 # This file
```

---

## 🔊 Example Alerts

* "Car detected at 120.0 meters."
* "Pedestrian detected. Please slow down."
* "Fog detected. Stop sign ahead. Prepare to slow down."

---

## 🧠 Customizing

* To add more classes: update `ui_main.py > generate_alerts()`
* To change alert frequency: modify polling interval (`root.after(3000, ...)`)
* To integrate weather: connect your weather API in





## 🎓 Atah Habibi – Developer

Role: Voice-Centric AI Assistant – Object Detection & Voice Feedback System

🧠 Methods

Used YOLOv5 with a pretrained best.pt model for object detection.

Webcam input processed via OpenCV.

GUI built with Tkinter; voice alerts via pyttsx3.

Outputs saved to inference_output.json.

📊 Results

Real-time detection and labeling of person, car, and traffic sign.

Alerts shown in GUI and spoken aloud.

JSON output updates every few seconds.

✅ Conclusion

Findings:

Working voice-assisted detection system with live feedback.

Limitations:

CPU-only; no GPU (Umar’s system).

Limited to 3 object classes.

Implications:

Useful for edge AI applications, accessibility tools.

Future work: more classes, weather-based decisions.

🔍 Introduction

Importance:

Real-time AI assistants improve awareness and safety.

What’s Missing:

Few tools combine detection + voice alerts locally.

Value Added:

Fills gap for lightweight, voice-driven object detection on local devices.

