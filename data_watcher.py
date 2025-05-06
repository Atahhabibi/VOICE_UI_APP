import json

def get_alert_data(path="inference_output.json"):
    with open(path, "r") as f:
        data = json.load(f)

    weather = data.get("weather", "Clear")
    objects = data.get("objects", [])

    alerts = []
    urgency = "green"

    if weather.lower() in ["fog", "storm"]:
        alerts.append(f"{weather} detected. Please drive carefully.")
        urgency = "yellow" if weather.lower() == "fog" else "red"

    for obj in objects:
        obj_class = obj.get("class", "Unknown")
        dist = obj.get("distance", "")
        if obj_class == "Pedestrian":
            alerts.append(f"Pedestrian detected at {dist}. Please slow down.")
            urgency = "red"
        elif obj_class == "Stop Sign" and weather.lower() == "fog":
            alerts.append(f"Fog and Stop Sign ahead at {dist}. Prepare to stop.")
            urgency = "red"

    color_map = {"green": "#ccffcc", "yellow": "#fffccc", "red": "#ffcccc"}
    return data, alerts, color_map.get(urgency, "white")
