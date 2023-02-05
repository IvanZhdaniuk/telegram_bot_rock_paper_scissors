from config_data.config import load_config

import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers.user_handlers import register_user_handlers
from handlers.other_handlers import register_user_othets_handlers

# инициализируем логгер
logger = logging.getLogger(__name__)

# функция для регистрации всех хендлеров
def register_all_handlers(dp: Dispatcher):
    register_user_othets_handlers(dp)
    register_user_handlers(dp)

# функция конфигурации и запуска бота
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер

    bot: Bot = Bot(token=config.tg_bot.token, parse_model='HTML')
    dp: Dispatcher = Dispatcher(bot)

    # ругистрируем все хэдлеры
    register_all_handlers(dp)

    # запускаем полинг
    try:
        await dp.start_poling()
    finally:
        await bot.close()

if __name__ == 'main':
    try:
        # запускаем функцию мэин
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # выводим в консоль собщения об ошибке
        # если получены исключения KeybordInput или SystemExit
        logger.error('Bot stopped!')

# Create object keyboards
# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)


# Create objects button
# keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#
# keyboard.row('1', '2', '3').row('4', '5', '6').insert('7')

# keyboard.add(KeyboardButton(text='send phone', request_contact=True))
# keyboard.add(KeyboardButton(text='send geolocation', request_location=True))
# keyboard.add(KeyboardButton(text='Create quizlet', request_poll=KeyboardButtonPollType()))
# keyboard.add(KeyboardButton(text='Start web app', web_app=WebAppInfo(url="https://stepik.org/")))

# button_1: KeyboardButton = KeyboardButton('Собак 🦮')
# button_2: KeyboardButton = KeyboardButton('Огурцов 🥒')


# adding buttons in keyboard
#keyboard.add(button_1, button_2, *[KeyboardButton(f'{i+1}') for i in range(300)])

# keyboard.add(button_1, button_2, 'button 3').add('button 4').add('button 5', 'button 6')

# This handler will respond to the "/start" command and send the keyboard to the chat
# async def process_start_command(message: types.Message):
#     await message.answer('Чего кошки боятся больше всего?',
# reply_markup=keyboard)
#
# # This handler will respond to the 'Собак" and delete the keyboard
# async def proces_dog_answer(message: types.Message):
#     await message.answer('Да, несомненно кошки боятся собак. Но вы видели как кошки '
#                          'боятся огурцов', reply_markup=ReplyKeyboardRemove())
#
# # This handler will respond to the 'Огурцов" and delete the keyboard
# async def proces_cats_answer(message: types.Message):
#     await message.answer('Да иногда кажется что огурчов кошки боятся больше.',
#                          reply_markup=ReplyKeyboardRemove())
#
# # Registered handler
# dp.register_message_handler(process_start_command, commands='start')
# dp.register_message_handler(proces_dog_answer, text='Собак 🦮')
# dp.register_message_handler(proces_cats_answer, text='Огурцов 🥒')
#
#

# print('BOT_TOKEN:', config.tg_bot.token)
# print('ADMIN_IDS:', config.tg_bot.admin_ids)
# print()
# print('DATABASE:', config.db.database)
# print('DB_HOST:', config.db.db_host)
# print('DB_USER:', config.db.db_user)
# print('DB_PASSWORD:', config.db.db_password)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
