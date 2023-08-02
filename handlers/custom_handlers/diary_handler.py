from telebot.types import Message
from loader import bot
from ..default_handlers.start import main_menu
from keyboards.reply.reply_keyboards import diary_markup, view_markup
from database.record_func import RecordIn


diary_commands = ['Training diary', 'Make an entry in the diary', 'View entry']
demonstrate_commands = ['View the last 10 entries', 'View multiple entries by numbers', 'View the entry by number']


def diary_entry(message):
    RecordIn.diary_entry(message.from_user.id, diary_entry=message.text)
    bot.send_message(message.from_user.id, text='Your note is saved')
    main_menu(message)


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
        ...
    elif message.text == 'View multiple entries by numbers':
        ...
    elif message.text == 'View the entry by number':
        ...
