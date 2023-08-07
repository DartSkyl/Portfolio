from telebot.types import Message
from database.get_func import RecordOut
from loader import bot


@bot.message_handler(commands=["request_history"])
def request_history(message: Message):
    RecordOut.last_ten_requests(message.from_user.id, bot)
