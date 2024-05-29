from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Нажми чтобы увидеть пейзаж')
    button2 = KeyboardButton('>')
    keyboard.add(button1,button2)
    return keyboard


def get_keyboard2():
    keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = KeyboardButton('Нажми чтобы увидеть увидеть приятного человека')
    button4 = KeyboardButton('<')
    keyboard2.add(button3,button4)
    return keyboard2


