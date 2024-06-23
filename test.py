import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import yookassa
from yookassa import Payment
import uuid
from payment import *
from aiogram import types
from payment import create, check
from aiogram.types import LabeledPrice
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import types

# Замените 'YOUR_BOT_TOKEN_HERE' на токен вашего бота
API_TOKEN = '7347714523:AAGZA_TNJOKz2RnUqiCx3wERx0zt3eS3vPI'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопка меню
menu_button = KeyboardButton('Меню')
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_button)

# Кнопка "Выбрать"
buy_products_button = KeyboardButton('Выбрать')
first_level_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(buy_products_button)

# Кнопки, которые появляются при нажатии на "Выбрать"
button1 = KeyboardButton('Купить продукт')
button2 = KeyboardButton('Бесплатный фрагмент')
button3 = KeyboardButton('Ещё продукты')
back_button = KeyboardButton('Вернуться обратно')
menu_button = KeyboardButton('Меню')
submenu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button1, button2, button3, back_button, menu_button)

# Кнопки для каждого товара
product1_button = KeyboardButton('Товар 1')
product2_button = KeyboardButton('Товар 2')
product3_button = KeyboardButton('Товар 3')
products_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(product1_button, product2_button, product3_button)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Нажми на кнопку 'Меню'.", reply_markup=menu_keyboard)

# Обработчик кнопки "Меню"
@dp.message_handler(lambda message: message.text == "Меню")
async def show_first_level_menu(message: types.Message):
    await message.answer("Выберите одну из кнопок ниже:", reply_markup=first_level_keyboard)

# Обработчик кнопки "Купить продукты"
@dp.message_handler(lambda message: message.text == "Выбрать")
async def show_products(message: types.Message):
    await message.answer("Выберите товар:", reply_markup=products_keyboard)

# Обработчики кнопок товаров
# Обработчики кнопок товаров
@dp.message_handler(lambda message: message.text == "Товар 1")
async def handle_product1(message: types.Message):
    await message.answer('Вы выбрали Товар 1. Доступные действия:', reply_markup=submenu_keyboard)

    # Добавляем уникальные записи для Товара 1
    await message.answer('Для Товара 1 доступны следующие действия:', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Купить продукт Товар 1'),
        KeyboardButton('Бесплатный фрагмент Товар 1'),
        KeyboardButton('Ещё продукты Товар 1'),
        back_button, 
        KeyboardButton('Меню')
    ))

@dp.message_handler(lambda message: message.text == "Товар 2")
async def handle_product2(message: types.Message):
    await message.answer('Вы выбрали Товар 2. Доступные действия:', reply_markup=submenu_keyboard)

    # Добавляем уникальные записи для Товара 2
    await message.answer('Для Товара 2 доступны следующие действия:', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Купить продукт Товар 2'),
        KeyboardButton('Бесплатный фрагмент Товар 2'),
        KeyboardButton('Ещё продукты Товар 2'),
        back_button,
        KeyboardButton('Меню')
    ))

@dp.message_handler(lambda message: message.text == "Товар 3")
async def handle_product3(message: types.Message):
    await message.answer('Вы выбрали Товар 3. Доступные действия:', reply_markup=submenu_keyboard)

    # Добавляем уникальные записи для Товара 3
    await message.answer('Для Товара 3 доступны следующие действия:', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Купить продукт Товар 3'),
        KeyboardButton('Бесплатный фрагмент Товар 3'),
        KeyboardButton('Ещё продукты Товар 3'),
        back_button,
        KeyboardButton('Меню')
    ))


# Обработчик кнопки "Вернуться обратно"
@dp.message_handler(lambda message: message.text == "Вернуться обратно")
async def go_back(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=products_keyboard)


@dp.message_handler(lambda message: message.text == "Купить продукт")
async def buy_product(message: types.Message):
    await message.answer('Вы можете приобрести продукт введя команду /buy')

@dp.message_handler(lambda message: message.text == "Бесплатный фрагмент")
async def buy_product(message: types.Message):
    await message.answer('Бесплатный фрагмент доступен по ссылке - https://www.youtube.com/')

@dp.message_handler(lambda message: message.text == "Ещё продукты")
async def buy_product(message: types.Message):
    await message.answer('Вот ещё наши продукты:\n1. Продукт 1\n2. Продукт 2')


#_________________________________________________________________________________
# Товар 1
@dp.message_handler(lambda message: message.text == "Купить продукт Товар 1")
async def buy_product(message: types.Message):
    await message.answer('Вы можете приобрести продукт введя команду /buy')

@dp.message_handler(lambda message: message.text == "Бесплатный фрагмент Товар 1")
async def buy_product(message: types.Message):
    await message.answer('Бесплатный фрагмент доступен по ссылке - https://www.youtube.com/')

@dp.message_handler(lambda message: message.text == "Ещё продукты Товар 1")
async def buy_product(message: types.Message):
    await message.answer('Вот ещё наши продукты:\n1. Продукт 1\n2. Продукт 2')


#_________________________________________________________________________________
# Товар 2
@dp.message_handler(lambda message: message.text == "Купить продукт Товар 2")
async def buy_product(message: types.Message):
    await message.answer('Вы можете приобрести продукт введя команду /buy')

@dp.message_handler(lambda message: message.text == "Бесплатный фрагмент Товар 2")
async def buy_product(message: types.Message):
    await message.answer('Бесплатный фрагмент доступен по ссылке - https://www.youtube.com/')

@dp.message_handler(lambda message: message.text == "Ещё продукты Товар 2")
async def buy_product(message: types.Message):
    await message.answer('Вот ещё наши продукты:\n1. Продукт 1\n2. Продукт 2')


#_________________________________________________________________________________
# Товар 3
@dp.message_handler(lambda message: message.text == "Купить продукт Товар 3")
async def buy_product(message: types.Message):
    await message.answer('Вы можете приобрести продукт введя команду /buy')

@dp.message_handler(lambda message: message.text == "Бесплатный фрагмент Товар 3")
async def buy_product(message: types.Message):
    await message.answer('Бесплатный фрагмент доступен по ссылке - https://www.youtube.com/')

@dp.message_handler(lambda message: message.text == "Ещё продукты Товар 3")
async def buy_product(message: types.Message):
    await message.answer('Вот ещё наши продукты:\n1. Продукт 1\n2. Продукт 2')







# Обработчик команды /buy
@dp.message_handler(commands=['buy'])
async def buy_handler(message: types.Message):
    sum_to_buy = 1000
    payment_url, payment_id = create(sum_to_buy, message.chat.id)

    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text='Оплатить',
        url=payment_url
    ))
    builder.add(types.InlineKeyboardButton(
        text='Проверить оплату',
        callback_data=f'check_{payment_id}'
    ))

    await message.answer(f"🟢Счет сформирован! Итого к оплате: {sum_to_buy}₽", reply_markup=builder)

# Обработчик колбэков проверки оплаты
@dp.callback_query_handler(lambda c: c.data.startswith('check_'))
async def check_handler(callback: types.CallbackQuery):
    payment_id = callback.data.split('_')[-1]
    result = check(payment_id)  # Предположим, что у вас есть функция для проверки оплаты
    if result:
        # Отправляем личное сообщение с информацией о платеже
        await bot.send_message(
            "1921428012",  # Ваш Telegram ID
            f"Прошла оплата:\n"
            f"id покупателя: user_chat_id\n"
            f"оплачено: yes\n"
            f"chat_id: {callback.message.chat.id}\n"
        )
        await bot.send_message(callback.message.chat.id, "Отлично, платёж прошёл! Вот ссылка на материал: https://www.youtube.com/")

        # Изменяем состояние кнопки на неактивное
        await bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=None  # Передаём None, чтобы убрать клавиатуру
        )

    else:
        await callback.message.answer('Оплата еще не прошла или возникла ошибка')
    await callback.answer()

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)