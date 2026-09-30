import json
import os

DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "fitness_data.json")


def initialize_data():
    """Create the data folder and file if they don't exist."""

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(DATA_FILE):
        default_data = {
            "workouts": [],
            "habits": []
        }

        with open(DATA_FILE, "w") as file:
            json.dump(default_data, file, indent=4)


def load_data():
    """Load fitness data from the JSON file."""

    initialize_data()

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return {
            "workouts": [],
            "habits": []
        }


def save_data(data):
    """Save fitness data to the JSON file."""

    initialize_data()

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)