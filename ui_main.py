import tkinter as tk
from tkinter import ttk
import json
import os
import time
from speech_engine import SpeechManager

# Initialize voice
speech = SpeechManager()

# GUI setup
root = tk.Tk()
root.title("Voice-Centric AI Assistant")
root.geometry("600x400")

status_label = ttk.Label(root, text="System Status: Running", foreground="green")
status_label.pack(pady=5)

detection_frame = ttk.LabelFrame(root, text="Live Detections")
detection_frame.pack(fill="both", expand=True, padx=10, pady=10)

detection_text = tk.Text(detection_frame, wrap="word", height=10)
detection_text.pack(fill="both", expand=True)

# Generate alert messages from data
def generate_alerts(data):
    weather = data.get("weather", "Clear")
    alerts = []

    if weather == "Fog":
        alerts.append("Severe fog detected. Please turn on high beams.")

    for obj in data.get("objects", []):
        cls = obj.get("class", "Unknown")
        distance = obj.get("distance", "N/A")

        # Filter out invalid distances
        try:
            dist_val = float(distance.replace("m", "").strip())
            if dist_val < 0:
                continue
        except:
            continue

        if cls == "Pedestrian":
            alerts.append("Pedestrian detected. Please slow down.")
        elif cls == "Stop Sign" and weather == "Fog":
            alerts.append("Fog detected. Stop sign ahead. Prepare to slow down.")
        elif cls == "car":
            alerts.append(f"Car detected at {distance}.")
        else:
            alerts.append(f"{cls} detected at {distance}.")

    return alerts

# Read JSON and update UI + voice
def poll_data():
    try:
        if os.path.exists("inference_output.json"):
            with open("inference_output.json") as f:
                data = json.load(f)

            detection_text.delete("1.0", tk.END)
            detection_text.insert(tk.END, f"Weather: {data.get('weather', 'N/A')}\n")

            for obj in data.get("objects", []):
                detection_text.insert(tk.END, f"Detected: {obj['class']} ({obj['distance']})\n")

            alerts = generate_alerts(data)
            print("📢 Alerts generated:", alerts)
            for alert in alerts:
                print(f"[VOICE] {alert}")
                speech.speak(alert)

    except Exception as e:
        print(f"[ERROR] {e}")

    root.after(3000, poll_data)

# Handle close event
def on_closing():
    speech.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start polling and GUI loop
poll_data()
root.mainloop()
