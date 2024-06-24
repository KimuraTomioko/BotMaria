import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from payment import create, check

# Замените 'YOUR_BOT_TOKEN_HERE' на токен вашего бота
API_TOKEN = '7230659353:AAHF66GIspjZTUoW_zPktwnXya0HNH1h70M'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопка меню
menu_button = KeyboardButton('Меню')
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_button)

# Кнопка "Купить продукты"
buy_products_button = KeyboardButton('Выбрать')
first_level_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(buy_products_button)

# Кнопки, которые появляются при нажатии на "Купить продукты"
submenu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Купить продукт'),
    KeyboardButton('Бесплатный фрагмент'),
    KeyboardButton('Ещё продукты'),
    KeyboardButton('Вернуться обратно'),
    KeyboardButton('Меню')
)

# Кнопки для каждого товара
products_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Гайд по страхам'),
    KeyboardButton('Гайд внутренний ребенок'),
    KeyboardButton('Консультация')
)

# Кнопки для "Гайд внутренний ребенок"
inner_child_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Просмотреть'),
    KeyboardButton('Ещё продукты'),
    KeyboardButton('Вернуться обратно'),
    KeyboardButton('Меню')
)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Нажми на кнопку 'Меню'.", reply_markup=menu_keyboard)

# Обработчик кнопки "Вернуться обратно"
@dp.message_handler(lambda message: message.text == "Вернуться обратно")
async def go_back(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=products_keyboard)

# Обработчик кнопки "Меню"
@dp.message_handler(lambda message: message.text == "Меню")
async def show_first_level_menu(message: types.Message):
    await message.answer("Выберите одну из кнопок ниже:", reply_markup=first_level_keyboard)

# Обработчик кнопки "Купить продукты"
@dp.message_handler(lambda message: message.text == "Выбрать")
async def show_products(message: types.Message):
    await message.answer("Выберите товар:", reply_markup=products_keyboard)

# Обработчики кнопок товаров
@dp.message_handler(lambda message: message.text in ["Гайд по страхам", "Гайд внутренний ребенок", "Консультация"])
async def handle_product(message: types.Message):
    product_name = message.text
    if product_name == "Консультация":
        await message.answer("Проконсультируйся со мной https://t.me/maryribakova")
    elif product_name == "Гайд внутренний ребенок":
        await message.answer(f'Вы выбрали {product_name}. Доступные действия:', reply_markup=inner_child_keyboard)
    else:
        await message.answer(f'Вы выбрали {product_name}. Доступные действия:', reply_markup=submenu_keyboard)

# Обработчики действий для каждого товара
@dp.message_handler(lambda message: message.text.startswith("Купить продукт"))
async def buy_product(message: types.Message):
    await message.answer('Вы можете приобрести продукт введя команду /buy')

@dp.message_handler(lambda message: message.text.startswith("Бесплатный фрагмент"))
async def free_fragment(message: types.Message):
    await message.answer('Бесплатный фрагмент доступен по ссылке - https://www.youtube.com/')

@dp.message_handler(lambda message: message.text.startswith("Ещё продукты"))
async def more_products(message: types.Message):
    await message.answer('Новые продукты пока что в разработке!')

@dp.message_handler(lambda message: message.text == "Просмотреть")
async def view_inner_child_guide(message: types.Message):
    await message.answer('Просмотреть материал можно по ссылке: https://t.me/rybakovanastavnik/128')

# Обработчик команды /buy
@dp.message_handler(commands=['buy'])
async def buy_handler(message: types.Message):
    sum_to_buy = 1000
    payment_url, payment_id = create(sum_to_buy, message.chat.id)

    builder = InlineKeyboardMarkup()
    builder.add(InlineKeyboardButton(
        text='Оплатить',
        url=payment_url
    ))
    builder.add(InlineKeyboardButton(
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
            callback.message.chat.id,
            "Отлично, платёж прошёл! Вот ссылка на материал: https://t.me/+arvnh2AOBodkYzEy"
        )

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
