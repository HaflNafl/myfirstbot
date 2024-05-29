from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Смотри на прикольный видосик рисование', url='https://youtu.be/4HyaDLpnDxM?si=a455bYcITNRxDexC')
    but_inline2 = InlineKeyboardButton('Слушай классную песню на ютубе', url='https://youtu.be/y2Fb4cEVyLU?si=m6q9_KMLVsdjtaJ1')
    keyboard_inline.add(but_inline,but_inline2)
    return keyboard_inline