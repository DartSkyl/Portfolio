from telebot.types import ReplyKeyboardMarkup


markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add('Выбрать тип тренировки')
markup.add('Установить уровень тренировки')
markup.add('Выбрать группу мышц')
markup.add('Посмотреть упражнения')
