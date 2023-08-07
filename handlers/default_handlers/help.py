from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    instruction = '1. To watch the exercises, you need to select all three parameters of the workout.\n' \
                  '2. You can record the result of the workout in a diary.\n' \
                  '3. You can view the entries in the diary in three different modes.\n' \
                  '4. To return to the main menu, use the command /main \n' \
                  '5. The /request_history command will show you the last ten queries.'
    text.append(instruction)
    bot.send_message(message.from_user.id, "\n".join(text))
