from loader import bot
import handlers  # noqa
from telebot import custom_filters
from database.model import create_tables
from utils.set_bot_commands import set_default_commands


if __name__ == "__main__":
    set_default_commands(bot)
    create_tables()
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling(skip_pending=True)
