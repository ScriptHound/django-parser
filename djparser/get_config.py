import json
import logging
from pathlib import Path
from logging import error
logging.basicConfig(level=logging.ERROR)

BASE_DIR = Path(__file__).resolve().parent


def get_config() -> dict:
    config = {}
    try:
        with open(BASE_DIR / 'db_credentials.json', 'r') as conf:
            config: dict = json.load(conf)
    except FileNotFoundError:
        error("DB config file not found")
    return config
