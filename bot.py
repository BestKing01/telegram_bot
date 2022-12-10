import time 
import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5842867498:AAFOg5o9MoYSHIxs9FkhNifJinSuNokFB0M"

MSG = "message work {}"

bot = Bot(token = TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])

async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    logging.info(f'{user_id}{user_name} {time.asctime()}')
    
    await message.reply(f"Привет, {user_name}")

    #10 раз будет отправлять MSG по 2 секнды
    for i in range(10):
        time.sleep(2)

        await bot.send_message(user_id, MSG.format(user_name))

if __name__ == '__main__':
    executor.start_polling(dp)