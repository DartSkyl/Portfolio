from telebot.types import Message
from loader import bot
from ..default_handlers.start import main_menu
from keyboards.reply.reply_keyboards import diary_markup, view_markup
from database.record_func import RecordIn
from database.get_func import RecordOut
from utils.misc.message_delet_func import delete_message


diary_commands = ['Training diary', 'Make an entry in the diary', 'View entry']
demonstrate_commands = ['View the last 10 entries', 'View multiple entries by numbers', 'View the entry by number']


def diary_entry(message):
    RecordIn.diary_entry(message.from_user.id, diary_entry=message.text)
    bot.send_message(message.from_user.id, text='Your note is saved')
    main_menu(message)
    delete_message(message.from_user.id, message.id, 8)


def viewing_range(message):
    try:
        user_range = [int(num) for num in message.text.split('-')]
        if len(user_range) != 2:
            raise ValueError('There should be only two numbers!')
        elif user_range[0] > user_range[1] or user_range[0] == user_range[1]:
            raise ValueError('The first number must be less than the second')
    except ValueError as error_message:
        error_msg = 'Input error!\n' + str(error_message) + '\n' + \
                    'Enter the viewing rang. Format: "1-10"'
        msg = bot.send_message(message.from_user.id, text=error_msg)
        bot.register_next_step_handler(msg, viewing_range)
    else:
        RecordOut.range_entry(message.from_user.id, user_range, bot)


def viewing_entry_by_number(message):
    try:
        user_number = int(message.text)
        if user_number > RecordOut.entry_count(message.from_user.id):
            raise ValueError('There is no record with this number!')
    except ValueError as error_message:
        error_msg = 'Input error!\n' + str(error_message) + '\n' + \
                    'Enter the entry number'
        msg = bot.send_message(message.from_user.id, text=error_msg)
        bot.register_next_step_handler(msg, viewing_entry_by_number)
    else:
        RecordOut.entry_by_number(message.from_user.id, user_number, bot)


@bot.message_handler(func=lambda message: message.text in diary_commands)
def diary_menu(message: Message):
    if message.text == 'Training diary':
        bot.send_message(message.from_user.id, text='Select the action', reply_markup=diary_markup)
    elif message.text == 'Make an entry in the diary':
        msg = bot.send_message(message.from_user.id, text='Enter a note')
        bot.register_next_step_handler(msg, diary_entry)
    elif message.text == 'View entry':
        bot.send_message(message.from_user.id, text='Choose a way to demonstrate', reply_markup=view_markup)


@bot.message_handler(func=lambda message: message.text in demonstrate_commands)
def diary_display(message: Message):
    if message.text == 'View the last 10 entries':
        RecordOut.print_last_ten_entry(message.from_user.id, bot)
    elif message.text == 'View multiple entries by numbers':
        mess_text = 'Enter the viewing rang. Format: "1-10"'
        msg = bot.send_message(message.from_user.id, text=mess_text)
        bot.register_next_step_handler(msg, viewing_range)
    elif message.text == 'View the entry by number':
        mess_text = 'Enter the entry number'
        msg = bot.send_message(message.from_user.id, text=mess_text)
        bot.register_next_step_handler(msg, viewing_entry_by_number)
