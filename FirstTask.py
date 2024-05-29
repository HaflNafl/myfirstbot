from aiogram import Bot, Dispatcher, types, executor
from config import TG_TOKEN
from Keyboard.keyboards import get_keyboard1,get_keyboard2
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Keyboard.KeyINline import key_inline



bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)







# async def set_commands(bot: Bot):
#     commands = [
#         types.BotCommand(command='/start', description='команда для активации'),
#         types.BotCommand(command='/help', description='команда для помощи чего то'),
#         types.BotCommand(command='/check', description='команда для проверки'),
#         types.BotCommand(command='/asas', description='команда для ыаволлыоаы'),
#         types.BotCommand(command='/boring', description='команда для веселья'),
#         types.BotCommand(command='/you_ve_been_cyberbullied', description='команда для моральной помощи'),
#         types.BotCommand(command='/dont_even_talk_to_me', description='бот отдыхает'),
#         types.BotCommand(command='/aaaaaaa', description='аааааааа')
#     ]
#     await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет', reply_markup=get_keyboard1())


@dp.message_handler(lambda message: message.text == 'Нажми чтобы увидеть увидеть приятного человека')
async def but(message: types.Message):
    await bot.send_photo(message.chat.id,
    photo='https://lirp.cdn-website.com/732b1648/dms3rep/multi/opt/kw-point-1920w.jpg', reply_markup=get_keyboard2())




@dp.message_handler(lambda message: message.text == 'Нажми чтобы увидеть пейзаж')
async def but(message: types.Message):
    await bot.send_photo(message.chat.id,
    photo='https://indasil.club/uploads/posts/2022-12/1669845532_15-indasil-club-p-legkii-peizazh-akvarelyu-vkontakte-16.jpg',
    caption='Это пейзаж нарисованный акварелью',
    reply_markup=key_inline())





@dp.message_handler(lambda message: message.text == '>')
async def but(message: types.Message):
     await message.answer('здесь могу показать на приятного человека', reply_markup=get_keyboard2())



@dp.message_handler(lambda message: message.text == '<')
async def but(message: types.Message):
     await message.answer('Просто верну к прошлым кнопкам ', reply_markup=get_keyboard1())






#
# @dp.message_handler(commands='help')
# async def help(message: types.Message):
#     await message.reply('Чем тебе помочь, совсем тупой?')
#
# @dp.message_handler(commands='check')
# async def check(message: types.Message):
#     await message.answer('Работает')
#
#
# @dp.message_handler(commands='asas')
# async def asas(message: types.Message):
#     await message.answer('fjfjjfjf')
#
#
# @dp.message_handler(commands='boring')
# async def boring(message: types.Message):
#     await message.answer('Иди по отжимайся')
#
#
#
# @dp.message_handler(commands='you_ve_been_cyberbullied')
# async def bulling(message: types.Message):
#     await message.answer('Ну не знаю , удали интернет')
#
#
# @dp.message_handler(commands='dont_even_talk_to_me')
# async def relax(message: types.Message):
#     await message.answer('Я тут не помощник')
#
#
# @dp.message_handler(commands='command')
# async def command(message: types.Message):
#     await message.answer('ААААААААА')





@dp.message_handler()
async def echo(message: types.Message):
     await message.answer(message.text)


# async def on_startup(dispatcher):
#     await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)