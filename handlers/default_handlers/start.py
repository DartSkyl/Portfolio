from telebot.types import Message
from loader import bot
from keyboards.reply.reply_keyboards import main_markup
from database.record_func import RecordIn
from database.get_func import RecordOut


def main_menu(message: Message):
    user_choice = RecordOut.last_request(message.from_user.id)
    text_message = f'Type of training: {user_choice[0].title()}\n' \
                   f'Training level: {user_choice[1].title()}\n' \
                   f'Muscle group: {user_choice[2].title()}\n'
    bot.send_message(message.from_user.id, text=text_message, reply_markup=main_markup)


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    if RecordOut.check_id(message.from_user.id):
        text = f'Welcome back, {message.from_user.first_name}!'
        bot.send_message(message.from_user.id, text=text)
        main_menu(message)
    else:
        RecordIn.regist_user(from_user_id=message.from_user.id, name=message.from_user.first_name)
        text = f'Congratulations, you`re on the right track, {message.from_user.first_name}'
        bot.send_message(message.from_user.id, text=text)
        main_menu(message)

# if __name__ == '__main__':
