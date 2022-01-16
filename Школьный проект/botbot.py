from random import *

import emoji
from aiogram import types, executor, Dispatcher, Bot

from d import act
from d18 import act18
from p import questions
from p18 import questions18
from t import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# bot

@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет ' + emoji.emojize(
        ':waving_hand:') + '\nЯ бот для игры "Правда или Действие"!\n\n' + emoji.emojize(
        ':robot:') + 'Мои команды:\n\n/truth - правда\n/action - действие\n/truth18 - правда 18+\n/action18 - действие '
                     '18+\n\nПравила:\n/info - ознакомься на всякий\n\nПожертвования:'
                     '\n/donate - поддержи автора на патрионе\n\nGOOD LUCK ' + emoji.emojize(':relieved_face:'))


@dp.message_handler(commands=['truth'])
async def truth_1(message: types.Message):
    await message.reply('Вопрос ' + emoji.emojize(':thinking_face:') + '\n' + choice(questions))


@dp.message_handler(commands=['action'])
async def dare_1(message: types.Message):
    await message.reply('Действие ' + emoji.emojize(':smirking_face:') + '\n' + choice(act))


@dp.message_handler(commands=['truth18'])
async def truth_2(message: types.Message):
    await message.reply(
        'Вопрос ' + emoji.emojize(':thinking_face:') + emoji.emojize(':no_one_under_eighteen:') + '\n' + choice(
            questions18))


@dp.message_handler(commands=['action18'])
async def dare_2(message: types.Message):
    await message.reply(
        'Действие ' + emoji.emojize(':smirking_face:') + emoji.emojize(':no_one_under_eighteen:') + '\n' + choice(
            act18))


@dp.message_handler(commands=['info'])
async def information(message: types.Message):
    await message.reply('Ты можешь использовать меня для игры в "Правда или действие" на тусовке, посиделке с '
                        'друзьями или в других иных ситуациях!\nМожешь создать беседу в Telegram со своими друзьями, '
                        'добавить меня и наслаждаться игрой онлайн! \n(Для успешной работы бота добавь его в '
                        'список админов беседы)')


@dp.message_handler(commands=['donate'])
async def dare_2(message: types.Message):
    await message.reply('Привет!\nПоддержи автора на патрионе https://www.patreon.com/prismgentem')

executor.start_polling(dp)
