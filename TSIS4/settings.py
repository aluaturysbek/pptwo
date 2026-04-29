import json

FILE = "settings.json"

def load_settings():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "snake_color": [0,200,0],
            "grid": True,
            "sound": True
        }

def save_settings(data):
    with open(FILE, "w") as f:
        json.dump(data, f)