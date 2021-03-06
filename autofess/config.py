import os
from dotenv import load_dotenv

CONFIG_FILE = "config.env"
if os.path.isfile(CONFIG_FILE):
    load_dotenv(CONFIG_FILE)

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
DATABASE_URL = os.getenv("DATABASE_URL")

TRIGGER_WORD = os.getenv("TRIGGER_WORD")
BLACKLIST_WORD = os.getenv("BLACKLIST_WORD")

SUCCESS_MESSAGE = os.getenv("SUCCESS_MESSAGE")
FILTERED_MESSAGE = os.getenv("FILTERED_MESSAGE")
ERROR_MESSAGE = os.getenv("ERROR_MESSAGE")
