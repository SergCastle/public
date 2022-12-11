from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from db import Database

db = Database('database.db')

#Главное меню
btnGame = KeyboardButton('🟢Начать')
btnProfile = KeyboardButton('👨‍🎓Профиль')
btnLeader = KeyboardButton('🏆Лидеры')
btnHelp = KeyboardButton('💬Помощь')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGame, btnProfile).add(btnLeader, btnHelp)


#Главное меню 2
btnA = KeyboardButton('A')
btnB = KeyboardButton('B')
btnC = KeyboardButton('C')
btnD = KeyboardButton('D')
btnBack = KeyboardButton('⬅️Назад')

mainMenu2 = ReplyKeyboardMarkup(resize_keyboard=True).row(btnA, btnB, btnC, btnD).add(btnBack)

#Главное меню 3
btnnextq = KeyboardButton('😃Продолжить')
btnBack = KeyboardButton('⬅️Назад')

mainMenu3 = ReplyKeyboardMarkup(resize_keyboard=True).row(btnnextq, btnBack)


#Инлайн обучение 1
ob1 = InlineKeyboardMarkup(row_width=1)

btnob1 = InlineKeyboardButton(text="Понятно", callback_data="btnob1")

ob1.add(btnob1)

#Инлайн выбор учебного заведения
MenuEducation = InlineKeyboardMarkup(row_width=1)

btned1 = InlineKeyboardButton(text="ЛГТУ", callback_data="btned1")
btned2 = InlineKeyboardButton(text="ЛМК", callback_data="btned2")
btned3 = InlineKeyboardButton(text="ЛКТиДХ", callback_data="btned3")
btned4 = InlineKeyboardButton(text="Другой", callback_data="btned4")

MenuEducation.add(btned1, btned2, btned3, btned4)

#Инлайн следующий
nextq = InlineKeyboardMarkup(row_width=1)

btnnextq = InlineKeyboardButton(text="Следующий вопрос", callback_data="btnnextq")

nextq.add(btnnextq)

#Инлайн ссылка
link = InlineKeyboardMarkup(row_width=1)

btnlink = InlineKeyboardButton(text="Узнать о ванаксиях НЛМК", callback_data="btnLinkScore")


link.add(btnlink)


