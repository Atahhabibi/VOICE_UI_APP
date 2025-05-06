# 🎙️ Voice-Centric AI Assistant (YOLOv5 + Tkinter)

This project is a voice-enabled desktop assistant that uses a trained YOLOv5 model to:
- Detect objects (like people, cars, traffic signs) in real time from your webcam
- Announce detections using speech synthesis
- Show live detection logs in a GUI
- Provide JSON output for other systems

---

## 📦 Features

- ✅ Real-time object detection via YOLOv5  
- ✅ Voice alerts using `pyttsx3`  
- ✅ Visual display using `tkinter`  
- ✅ JSON file output for integration

---

## 🖥️ UI Components

| Section         | Description                                          |
|-----------------|------------------------------------------------------|
| Top Bar         | System status (e.g., Running)                        |
| Detection Panel | Text area showing real-time detections               |
| Voice Alerts    | Spoken feedback like “Car detected at 50 meters”     |

---

## 🛠 Installation

1. **Clone the Repo**
   ```bash
   git clone <your-repo-url>
   cd voice_ui_app



Create Virtual Environment

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Add your YOLOv5 model
Place your best.pt model in the root directory.

▶️ Running the App
1. Start Webcam Detection
bash
Copy
Edit
python inference_runner.py
This script:

Loads the YOLOv5 model

Opens your webcam

Draws bounding boxes

Outputs inference_output.json

2. Start the UI + Voice Assistant
bash
Copy
Edit
python ui_main.py
This script:

Displays the GUI

Monitors inference_output.json

Speaks context-aware alerts








