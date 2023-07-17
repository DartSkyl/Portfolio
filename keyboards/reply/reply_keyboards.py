from telebot.types import ReplyKeyboardMarkup, KeyboardButton


markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
button_1 = KeyboardButton(text='Выбрать тип тренировки')
button_2 = KeyboardButton(text='Установить уровень тренировки')
button_3 = KeyboardButton(text='Выбрать группу мышц')
button_4 = KeyboardButton(text='Посмотреть упражнения')
markup.add(button_1, button_2, button_3, button_4)
