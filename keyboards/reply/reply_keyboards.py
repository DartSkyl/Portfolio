from telebot.types import ReplyKeyboardMarkup, KeyboardButton


main_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)  # Main menu keyboard
button_1: KeyboardButton = KeyboardButton(text='Choose the type of training')
button_2: KeyboardButton = KeyboardButton(text='Set the training level')
button_3: KeyboardButton = KeyboardButton(text='Choose a muscle group')
button_4: KeyboardButton = KeyboardButton(text='View exercises')
button_5: KeyboardButton = KeyboardButton(text='Training diary')
main_markup.add(button_1, button_2, button_3, button_4, button_5)

diary_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)   # Diary action menu
view_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)  # Selecting display option
d_butt_1: KeyboardButton = KeyboardButton(text='Make an entry in the diary')
d_butt_2: KeyboardButton = KeyboardButton(text='View entry')
d_butt_3: KeyboardButton = KeyboardButton(text='View the last 10 entries')
d_butt_4: KeyboardButton = KeyboardButton(text='View multiple entries by numbers')
d_butt_5: KeyboardButton = KeyboardButton(text='View the entry by number')
diary_markup.add(d_butt_1, d_butt_2)
view_markup.add(d_butt_3, d_butt_4, d_butt_5)
