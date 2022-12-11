from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# главное меню
btnTarot = KeyboardButton('Гадать')
btnProfile = KeyboardButton('Профиль')
btnDeck = KeyboardButton('Колода')
btnHelp = KeyboardButton('Помощь')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnTarot, btnDeck).add(btnProfile, btnHelp)


#Инлайн клавиатура выбор категории
category = InlineKeyboardMarkup(row_width=2)

btnAll = InlineKeyboardButton(text="Общая", callback_data="btnAll")
btnWork = InlineKeyboardButton(text="Работа", callback_data="btnWork")
btnLove = InlineKeyboardButton(text="Любовь", callback_data="btnLove")
btnPersona = InlineKeyboardButton(text="Личность", callback_data="btnPersona")

category.add(btnAll, btnWork, btnLove, btnPersona)


#Инлайн клавиатура выбор колоды
deck = InlineKeyboardMarkup(row_width=3)

btnRayder = InlineKeyboardButton(text="Рейдер Уайт", callback_data="btnRayder")
btnDoor = InlineKeyboardButton(text="78 дверей", callback_data="btnDoor")
btnTot = InlineKeyboardButton(text="Тот", callback_data="btnTot")

deck.add(btnRayder, btnDoor, btnTot)