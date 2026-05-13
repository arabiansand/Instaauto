from dotenv import load_dotenv
import os
import json

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.json")

with open(CONFIG_PATH, "r") as f:
    CONFIG = json.load(f)

ENV = {
    "IG_USERNAME": os.getenv("IG_USERNAME"),
    "IG_PASSWORD": os.getenv("IG_PASSWORD"),
    "HEADLESS": os.getenv("HEADLESS", "true")
}
