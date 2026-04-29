import json

# ---------------- SETTINGS ----------------
def save_settings(data):
    with open("settings.json", "w") as f:
        json.dump(data, f, indent=4)

def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except:
        return {"sound": True, "difficulty": "normal", "color": "red"}


# ---------------- LEADERBOARD ----------------
def save_score(name, score, distance):
    try:
        with open("leaderboard.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "name": name,
        "score": score,
        "distance": distance
    })

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open("leaderboard.json", "w") as f:
        json.dump(data, f, indent=4)


def load_scores():
    try:
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    except:
        return []