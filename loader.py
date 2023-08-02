from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)

api_url = config.API_URL
api_headers = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": config.HOST_API
}
