from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["write"])
def bot_start(message: Message):
    bot.reply_to(message, f"Здесь {message.from_user.full_name} ведет запись в дневник!")
