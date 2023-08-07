import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
HOST_API = os.getenv("HOST_API")
API_URL = os.getenv("API_URL")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("main", "Return to the main menu"),
    ("help", "Output help"),
    ("request_history", "Get last 10 requests")
)
