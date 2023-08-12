from typing import List
from telebot.types import Message
from loader import bot
from ..default_handlers.start import main_menu
from keyboards.reply.reply_keyboards import diary_markup, view_markup
from database.record_func import RecordIn
from database.get_func import RecordOut
from utils.misc.message_delet_func import delete_message


# List of commands for interacting with the training diary
diary_commands: List[str] = ['Training diary', 'Make an entry in the diary', 'View entry']
# The list is a command for viewing entries in the diary
viewing_comm: List[str] = ['View the last 10 entries', 'View multiple entries by numbers', 'View the entry by number']


def diary_entry(message: Message):
    """
    Function saves the diary entry that the user entered
    :param message: A message with a user entry
    """
    RecordIn.diary_entry(message.from_user.id, diary_entry=message.text)
    bot.send_message(message.from_user.id, text='Your note is saved')
    main_menu(message)  # After saving the entry, bot returns the user to the main menu
    delete_message(message.from_user.id, message.id, 8)  # And cleans the message history


def viewing_range(message: Message):
    """
    Function output entries from the user`s diary by range. First, the correctness of the range input is checked
    :param message: Message with user range
    """
    try:  # Checking the correctness of the range
        user_range: List[int] = [int(num) for num in message.text.split('-')]
        if len(user_range) != 2:
            raise ValueError('There should be only two numbers!')
        elif user_range[0] > user_range[1] or user_range[0] == user_range[1]:
            raise ValueError('The first number must be less than the second')

    # If an error occurs, we poison the user with the appropriate message
    except ValueError as error_message:
        error_msg: str = 'Input error!\n' + str(error_message) + '\n' + \
                    'Enter the viewing rang. Format: "1-10"'
        msg: Message = bot.send_message(message.from_user.id, text=error_msg)  # And we ask the user to try again
        bot.register_next_step_handler(msg, viewing_range)

    else:   # If everything all right, then we output the records
        RecordOut.range_entry(message.from_user.id, user_range, bot)


def viewing_entry_by_number(message):
    """
    Function output an entry from the user`s diary by number
    :param message: Message with the user`s entry number
    """
    try:  # Checking the correctness of the number
        user_number: int = int(message.text)
        if user_number > RecordOut.entry_count(message.from_user.id):
            raise ValueError('There is no record with this number!')

    # If an error occurs, we poison the user with the appropriate message
    except ValueError as error_message:
        error_msg: str = 'Input error!\n' + str(error_message) + '\n' + \
                    'Enter the entry number'
        msg: Message = bot.send_message(message.from_user.id, text=error_msg)  # And we ask the user to try again
        bot.register_next_step_handler(msg, viewing_entry_by_number)

    else:  # If everything all right, then we output the record
        RecordOut.entry_by_number(message.from_user.id, user_number, bot)


@bot.message_handler(func=lambda message: message.text in diary_commands)
def diary_menu(message: Message):
    """
    Handler processing commands for interacting with the diary
    :param message: Message with the command
    """
    if message.text == 'Training diary':
        bot.send_message(message.from_user.id, text='Select the action', reply_markup=diary_markup)
    elif message.text == 'Make an entry in the diary':
        msg: Message = bot.send_message(message.from_user.id, text='Enter a note')
        bot.register_next_step_handler(msg, diary_entry)  # Bot catches a message with a user record
    elif message.text == 'View entry':
        bot.send_message(message.from_user.id, text='Choose a way to demonstrate', reply_markup=view_markup)


@bot.message_handler(func=lambda message: message.text in viewing_comm)
def diary_display(message: Message):
    """
    Handler that processes commands with the record view mode
    :param message: Message with the command
    """
    if message.text == 'View the last 10 entries':
        RecordOut.print_last_ten_entry(message.from_user.id, bot)
    elif message.text == 'View multiple entries by numbers':
        mess_text = 'Enter the viewing rang. Format: "1-10"'
        msg: Message = bot.send_message(message.from_user.id, text=mess_text)
        bot.register_next_step_handler(msg, viewing_range)  # Bot catches a message with a user range
    elif message.text == 'View the entry by number':
        mess_text = 'Enter the entry number'
        msg: Message = bot.send_message(message.from_user.id, text=mess_text)
        bot.register_next_step_handler(msg, viewing_entry_by_number)  # Bot catches a message with a user number
