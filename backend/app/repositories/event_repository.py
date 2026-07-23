import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "events.json"


class EventRepository:

    @staticmethod
    def load_events():

        with open(DATA_FILE, "r", encoding="utf-8") as file:

            data = json.load(file)

        return data.get("events", [])