import logging

from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from db import Database
from create_bot import dp, bot
from aiogram.types.message import ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import link
from os import path

import time
import datetime

logging.basicConfig(level=logging.INFO)

def get_script_dir():
    abs_path = path.abspath(__file__)
    return path.dirname(abs_path)

DB_NAME = 'databasequiz.db'
DB_FILE = get_script_dir() + path.sep + DB_NAME

db = Database(DB_FILE)
    


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Привет!\nДобро пожаловать в *викторину НЛМК*! Напиши, как мне к тебе обращаться?", parse_mode="Markdown")
    else:
        await bot.send_message(message.from_user.id, "Ты уже зарегистрирован! Выбери, что хочешь сделать", reply_markup=nav.mainMenu)

@dp.message_handler(commands=['commands'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        qcount = str(db.get_qcount(message.from_user.id))
        lcount = str(db.get_lcount(message.from_user.id))
        losecount = str(db.get_lose(message.from_user.id))
        hr = str(db.get_hr(message.from_user.id))
                    
        await bot.send_message(message.from_user.id, "Кол-во вопросов: " + qcount + "\nКол-во лидеров: " + lcount + "\nСсылка на HH: " + hr + "\nОбъяснения: " + losecount + "\n--------------------------------\nadmin4220 - стать администратором\nsendall - через пробел текст сообщения, отправить всем сообщение\nstats - статистика пользователей\nreset - сбросить регистрацию у админа\nresetall - через пробел название места проведения, сбросить викторину и всех участников\nq15 - установить 15 вопросов викторины\nq21 - установить 21 вопросов викторины\nl10 - установить 10 лидеров викторины\nl25 - установить 25 лидеров викторины\nleaders - список победителей\nhr1 - включить ссылку на hh\nhr0 - выключить ссылку на hh\nlose1 - включить объяснения при ошибках\nlose0 - выключить объяснения при ошибках", parse_mode="Markdown")
    
@dp.message_handler(commands=['reset'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_admin(message.from_user.id, "reset")
        db.set_reset(message.from_user.id, 1)
        await bot.send_message(message.from_user.id, "регистрация сброшена, перезапусти викторину /start", parse_mode="Markdown")

@dp.message_handler(commands=['leaders'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        
            qcount = str(db.get_qcount(message.from_user.id))
            lcount = db.get_lcount(message.from_user.id)
            leaderscore = db.get_leaderscore(message.from_user.id)
            
            if lcount == 10:
                leader = "\n1." + str (leaderscore[0][0]) + " #" + str (leaderscore[0][2]) 
                leader1 = "\n2." + str (leaderscore[1][0]) + " #" + str (leaderscore[1][2])
                leader2 = "\n3." + str (leaderscore[2][0]) + " #" + str (leaderscore[2][2])
                leader3 = "\n4." + str (leaderscore[3][0]) + " #" + str (leaderscore[3][2])
                leader4 = "\n5." + str (leaderscore[4][0]) + " #" + str (leaderscore[4][2])
                leader5 = "\n6." + str (leaderscore[5][0]) + " #" + str (leaderscore[5][2])
                leader6 = "\n7." + str (leaderscore[6][0]) + " #" + str (leaderscore[6][2])
                leader7 = "\n8." + str (leaderscore[7][0]) + " #" + str (leaderscore[7][2])
                leader8 = "\n9." + str (leaderscore[8][0]) + " #" + str (leaderscore[8][2])
                leader9 = "\n10." + str (leaderscore[9][0]) + " #" + str (leaderscore[9][2])
                
                await bot.send_message(message.from_user.id, "Лидеры: " + leader + leader1 + leader2 + leader3 + leader4 + leader5 + leader6 + leader7 + leader8 + leader9)


            if lcount == 25:
                leader = "\n1." + str (leaderscore[0][0]) + " #" + str (leaderscore[0][2])
                leader1 = "\n2." + str (leaderscore[1][0]) + " #" + str (leaderscore[1][2])
                leader2 = "\n3." + str (leaderscore[2][0]) + " #" + str (leaderscore[2][2])
                leader3 = "\n4." + str (leaderscore[3][0]) + " #" + str (leaderscore[3][2])
                leader4 = "\n5." + str (leaderscore[4][0]) + " #" + str (leaderscore[4][2])
                leader5 = "\n6." + str (leaderscore[5][0]) + " #" + str (leaderscore[5][2])
                leader6 = "\n7." + str (leaderscore[6][0]) + " #" + str (leaderscore[6][2])
                leader7 = "\n8." + str (leaderscore[7][0]) + " #" + str (leaderscore[7][2])
                leader8 = "\n9." + str (leaderscore[8][0]) + " #" + str (leaderscore[8][2])
                leader9 = "\n10." + str (leaderscore[9][0]) + " #" + str (leaderscore[9][2])
                leader10 = "\n11." + str (leaderscore[10][0]) + " #" + str (leaderscore[10][2])
                leader11 = "\n12." + str (leaderscore[11][0]) + " #" + str (leaderscore[11][2])
                leader12 = "\n13." + str (leaderscore[12][0]) + " #" + str (leaderscore[12][2])
                leader13 = "\n14." + str (leaderscore[13][0]) + " #" + str (leaderscore[13][2])
                leader14 = "\n15." + str (leaderscore[14][0]) + " #" + str (leaderscore[14][2])
                leader15 = "\n16." + str (leaderscore[15][0]) + " #" + str (leaderscore[15][2])
                leader16 = "\n17." + str (leaderscore[16][0]) + " #" + str (leaderscore[16][2])
                leader17 = "\n18." + str (leaderscore[17][0]) + " #" + str (leaderscore[17][2])
                leader18 = "\n19." + str (leaderscore[18][0]) + " #" + str (leaderscore[18][2])
                leader19 = "\n20." + str (leaderscore[19][0]) + " #" + str (leaderscore[19][2])
                leader20 = "\n21." + str (leaderscore[20][0]) + " #" + str (leaderscore[20][2])
                leader21 = "\n22." + str (leaderscore[21][0]) + " #" + str (leaderscore[21][2])
                leader22 = "\n23." + str (leaderscore[22][0]) + " #" + str (leaderscore[22][2])
                leader23 = "\n24." + str (leaderscore[23][0]) + " #" + str (leaderscore[23][2])
                leader24 = "\n25." + str (leaderscore[24][0]) + " #" + str (leaderscore[24][2])
                
                await bot.send_message(message.from_user.id, "Лидеры: " + leader + leader1 + leader2 + leader3 + leader4 + leader5 + leader6 + leader7 + leader8 + leader9 + leader10 + leader11 + leader12 + leader13 + leader14 + leader15 + leader16 + leader17 + leader18 + leader19 + leader20 + leader21 + leader22 + leader23 + leader24)


@dp.message_handler(commands=['lose1'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_lose(message.from_user.id, 1)
        await bot.send_message(message.from_user.id, "Объяснения при проигрышах включены", parse_mode="Markdown")

@dp.message_handler(commands=['lose0'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_lose(message.from_user.id, 0)
        await bot.send_message(message.from_user.id, "Объяснения при проигрышах выключены", parse_mode="Markdown")

@dp.message_handler(commands=['hr1'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_hr(message.from_user.id, 1)
        await bot.send_message(message.from_user.id, "ссылка на HH включена", parse_mode="Markdown")

@dp.message_handler(commands=['hr0'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_hr(message.from_user.id, 0)
        await bot.send_message(message.from_user.id, "ссылка на HH выключена", parse_mode="Markdown")
                         
@dp.message_handler(commands=['q15'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_qcount(message.from_user.id, 15)
        await bot.send_message(message.from_user.id, "Установлено кол-во вопросов - 15", parse_mode="Markdown")

@dp.message_handler(commands=['q21'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_qcount(message.from_user.id, 21)
        await bot.send_message(message.from_user.id, "Установлено кол-во вопросов - 21", parse_mode="Markdown")
        
@dp.message_handler(commands=['l10'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_lcount(message.from_user.id, 10)
        await bot.send_message(message.from_user.id, "Установлено кол-во лидеров - 10", parse_mode="Markdown")        


@dp.message_handler(commands=['l25'])
async def start(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        db.set_lcount(message.from_user.id, 25)
        await bot.send_message(message.from_user.id, "Установлено кол-во лидеров - 25", parse_mode="Markdown") 

#@dp.message_handler(commands=['l50'])
#async def start(message: types.Message):
#    if db.get_admin(message.from_user.id) == 'admin':
#        db.set_lcount(message.from_user.id, 50)
#        await bot.send_message(message.from_user.id, "Установлено кол-во лидеров - 50", parse_mode="Markdown") 

@dp.message_handler(commands=['stats'])
async def admin(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        statsnumberusers = int(db.get_numberusers(message.from_user.id)[0][0]) - 50
        statsnumberusers1 = "Кол-во пользователей: " + str(statsnumberusers)
        
        #statsnumberusers2 = int(db.get_numberusers2(message.from_user.id)[0][0]) - 3
        #statsnumberusers21 = "\nЛГТУ: " + str(statsnumberusers2)

        #statsnumberusers3 = int(db.get_numberusers3(message.from_user.id)[0][0]) - 3
        #statsnumberusers31 = "\nЛМК: " + str(statsnumberusers3)

        #statsnumberusers4 = int(db.get_numberusers4(message.from_user.id)[0][0]) - 3
        #statsnumberusers41 = "\nЛКТиДХ: " + str(statsnumberusers4)

        #statsnumberusers5 = int(db.get_numberusers5(message.from_user.id)[0][0]) - 3
        #statsnumberusers51 = "\nДругой: " + str(statsnumberusers5)
        
        stats1 = "\nКол-во игр: " + str(db.get_stats1(message.from_user.id))
        
        statslink = "\nКол-во переходов на HH: " + str(db.get_statslinkscore(message.from_user.id))
        
        #leaderscore = db.get_leaderscore(message.from_user.id)               

        #await bot.send_message(message.from_user.id, "Лидеры: " + leaderscore )
        await bot.send_message(message.from_user.id, statsnumberusers1 + stats1 + statslink)


@dp.message_handler(commands=['sendall'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if db.get_admin(message.from_user.id) == 'admin':
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)
            
            await bot.send_message(message.from_user.id, "Успешная рассылка")


@dp.message_handler(commands=['resetall'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if db.get_admin(message.from_user.id) == 'admin':
            text = message.text[10:]
            users = db.get_usersnew()
            for row in users:
                try:
                    db.set_admin(row[0], text)
                    db.set_reset(row[0], 1)
                except:
                    pass
            
            db.set_stats1(message.from_user.id, 0)
            db.set_statslinkscore(message.from_user.id, 0)
            await bot.send_message(message.from_user.id, "Викторина успешно перезапущена")


@dp.message_handler(commands=['admin4220'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        db.set_admin(message.from_user.id, "admin")
        await bot.send_message(message.from_user.id, "Теперь ты администратор викторины, тебе доступны следующие команды /commands")

        
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '🟢Начать':
            
            if str (db.get_finish(message.from_user.id)) == "yes":
                leaderscore = db.get_leaderscore(message.from_user.id)
                userscoreall = db.get_scoreall(message.from_user.id)
                qcount = str(db.get_qcount(message.from_user.id))
                await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                if db.get_hr(message.from_user.id) == 1:
                    await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link)    

            if int (db.get_questioncount(message.from_user.id)) == 1:
#общая статистика игр    
                stats1 = db.get_stats1(message.from_user.id)
                stats11 = int(stats1) + 1
    
                db.set_stats1(message.from_user.id, stats11)
            
# Отправляем вопрос и записываем правильный ответ в таблицу                
                questionanswer = await db.get_questionanswer(message.from_user.id)
                questionanswer2 = questionanswer[0]
                
                answerwin =  questionanswer2[0]
                answerwinstr = str (answerwin)

                db.set_answerwinusers(message.from_user.id, answerwinstr)

# Записываем время начала прохождения                 
                time1 = int(time.time())
                db.set_time1(message.from_user.id, time1)
                      
                await db.get_question(message)
            
            else:
                
                if str (db.get_finish(message.from_user.id)) == "yes":
                    pass
#                    leaderscore = db.get_leaderscore(message.from_user.id)
#                    userscoreall = db.get_scoreall(message.from_user.id)
               
#                    await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/32 вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                    
                else:
#общая статистика игр    
                    stats1 = db.get_stats1(message.from_user.id)
                    stats11 = int(stats1) + 1
    
                    db.set_stats1(message.from_user.id, stats11)
            
# Отправляем вопрос и записываем правильный ответ в таблицу                
                    questionanswer = await db.get_questionanswer(message.from_user.id)
                    questionanswer2 = questionanswer[0]
                
                    answerwin =  questionanswer2[0]
                    answerwinstr = str (answerwin)

                    db.set_answerwinusers(message.from_user.id, answerwinstr)
                      
                    await db.get_question(message)
                

        elif message.text == '👨‍🎓Профиль':

                user_nickname = "Имя: " + str(db.get_nickname(message.from_user.id)) + " #" + str(db.get_idplayer(message.from_user.id))
                users_scoretime = db.get_time2(message.from_user.id)
                tf = str(datetime.timedelta(seconds=users_scoretime))
                tf = tf.replace("days", "дней")
                tf = tf.replace("day", "день")
                qcount = str(db.get_qcount(message.from_user.id))
                user_scoreall = "\nПравильных ответов: " + str(db.get_scoreall(message.from_user.id)) + "/" + qcount + "(" + tf + ")"          
                await bot.send_message(message.from_user.id, user_nickname + user_scoreall)
            
        elif message.text == '🏆Лидеры':
            qcount = str(db.get_qcount(message.from_user.id))
            lcount = db.get_lcount(message.from_user.id)
            leaderscore = db.get_leaderscore(message.from_user.id)
            
            if lcount == 10:
                leader = "\n1." + str (leaderscore[0][0]) + " #" + str (leaderscore[0][2]) + " - " + str (leaderscore[0][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[0][3]))) + ")"
                leader1 = "\n2." + str (leaderscore[1][0]) + " #" + str (leaderscore[1][2]) + " - " + str (leaderscore[1][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[1][3]))) + ")"
                leader2 = "\n3." + str (leaderscore[2][0]) + " #" + str (leaderscore[2][2]) + " - " + str (leaderscore[2][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[2][3]))) + ")"
                leader3 = "\n4." + str (leaderscore[3][0]) + " #" + str (leaderscore[3][2]) + " - " + str (leaderscore[3][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[3][3]))) + ")"
                leader4 = "\n5." + str (leaderscore[4][0]) + " #" + str (leaderscore[4][2]) + " - " + str (leaderscore[4][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[4][3]))) + ")"
                leader5 = "\n6." + str (leaderscore[5][0]) + " #" + str (leaderscore[5][2]) + " - " + str (leaderscore[5][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[5][3]))) + ")"
                leader6 = "\n7." + str (leaderscore[6][0]) + " #" + str (leaderscore[6][2]) + " - " + str (leaderscore[6][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[6][3]))) + ")"
                leader7 = "\n8." + str (leaderscore[7][0]) + " #" + str (leaderscore[7][2]) + " - " + str (leaderscore[7][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[7][3]))) + ")"
                leader8 = "\n9." + str (leaderscore[8][0]) + " #" + str (leaderscore[8][2]) + " - " + str (leaderscore[8][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[8][3]))) + ")"
                leader9 = "\n10." + str (leaderscore[9][0]) + " #" + str (leaderscore[9][2]) + " - " + str (leaderscore[9][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[9][3]))) + ")"
                
                await bot.send_message(message.from_user.id, "Лидеры: " + leader + leader1 + leader2 + leader3 + leader4 + leader5 + leader6 + leader7 + leader8 + leader9)


            if lcount == 25:
                leader = "\n1." + str (leaderscore[0][0]) + " #" + str (leaderscore[0][2]) + " - " + str (leaderscore[0][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[0][3]))) + ")"
                leader1 = "\n2." + str (leaderscore[1][0]) + " #" + str (leaderscore[1][2]) + " - " + str (leaderscore[1][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[1][3]))) + ")"
                leader2 = "\n3." + str (leaderscore[2][0]) + " #" + str (leaderscore[2][2]) + " - " + str (leaderscore[2][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[2][3]))) + ")"
                leader3 = "\n4." + str (leaderscore[3][0]) + " #" + str (leaderscore[3][2]) + " - " + str (leaderscore[3][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[3][3]))) + ")"
                leader4 = "\n5." + str (leaderscore[4][0]) + " #" + str (leaderscore[4][2]) + " - " + str (leaderscore[4][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[4][3]))) + ")"
                leader5 = "\n6." + str (leaderscore[5][0]) + " #" + str (leaderscore[5][2]) + " - " + str (leaderscore[5][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[5][3]))) + ")"
                leader6 = "\n7." + str (leaderscore[6][0]) + " #" + str (leaderscore[6][2]) + " - " + str (leaderscore[6][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[6][3]))) + ")"
                leader7 = "\n8." + str (leaderscore[7][0]) + " #" + str (leaderscore[7][2]) + " - " + str (leaderscore[7][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[7][3]))) + ")"
                leader8 = "\n9." + str (leaderscore[8][0]) + " #" + str (leaderscore[8][2]) + " - " + str (leaderscore[8][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[8][3]))) + ")"
                leader9 = "\n10." + str (leaderscore[9][0]) + " #" + str (leaderscore[9][2]) + " - " + str (leaderscore[9][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[9][3]))) + ")"
                leader10 = "\n11." + str (leaderscore[10][0]) + " #" + str (leaderscore[10][2]) + " - " + str (leaderscore[10][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[10][3]))) + ")"
                leader11 = "\n12." + str (leaderscore[11][0]) + " #" + str (leaderscore[11][2]) + " - " + str (leaderscore[11][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[11][3]))) + ")"
                leader12 = "\n13." + str (leaderscore[12][0]) + " #" + str (leaderscore[12][2]) + " - " + str (leaderscore[12][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[12][3]))) + ")"
                leader13 = "\n14." + str (leaderscore[13][0]) + " #" + str (leaderscore[13][2]) + " - " + str (leaderscore[13][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[13][3]))) + ")"
                leader14 = "\n15." + str (leaderscore[14][0]) + " #" + str (leaderscore[14][2]) + " - " + str (leaderscore[14][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[14][3]))) + ")"
                leader15 = "\n16." + str (leaderscore[15][0]) + " #" + str (leaderscore[15][2]) + " - " + str (leaderscore[15][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[15][3]))) + ")"
                leader16 = "\n17." + str (leaderscore[16][0]) + " #" + str (leaderscore[16][2]) + " - " + str (leaderscore[16][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[16][3]))) + ")"
                leader17 = "\n18." + str (leaderscore[17][0]) + " #" + str (leaderscore[17][2]) + " - " + str (leaderscore[17][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[17][3]))) + ")"
                leader18 = "\n19." + str (leaderscore[18][0]) + " #" + str (leaderscore[18][2]) + " - " + str (leaderscore[18][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[18][3]))) + ")"
                leader19 = "\n20." + str (leaderscore[19][0]) + " #" + str (leaderscore[19][2]) + " - " + str (leaderscore[19][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[19][3]))) + ")"
                leader20 = "\n21." + str (leaderscore[20][0]) + " #" + str (leaderscore[20][2]) + " - " + str (leaderscore[20][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[20][3]))) + ")"
                leader21 = "\n22." + str (leaderscore[21][0]) + " #" + str (leaderscore[21][2]) + " - " + str (leaderscore[21][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[21][3]))) + ")"
                leader22 = "\n23." + str (leaderscore[22][0]) + " #" + str (leaderscore[22][2]) + " - " + str (leaderscore[22][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[22][3]))) + ")"
                leader23 = "\n24." + str (leaderscore[23][0]) + " #" + str (leaderscore[23][2]) + " - " + str (leaderscore[23][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[23][3]))) + ")"
                leader24 = "\n25." + str (leaderscore[24][0]) + " #" + str (leaderscore[24][2]) + " - " + str (leaderscore[24][1]) + "/" + qcount + " (" + str(datetime.timedelta(seconds = (leaderscore[24][3]))) + ")"
                
                await bot.send_message(message.from_user.id, "Лидеры: " + leader + leader1 + leader2 + leader3 + leader4 + leader5 + leader6 + leader7 + leader8 + leader9 + leader10 + leader11 + leader12 + leader13 + leader14 + leader15 + leader16 + leader17 + leader18 + leader19 + leader20 + leader21 + leader22 + leader23 + leader24)
                         
                         
        elif message.text == '💬Помощь':
            if db.get_learn(message.from_user.id) == 'setlearn':
                await bot.send_message(message.from_user.id, "Нажми на 🟢Начать", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "Если возникли проблемы с игрой или есть вопросы, пожалуйста обратись на стенд НЛМК!", reply_markup=nav.mainMenu) 
        
 
        elif message.text == 'A':
            if db.get_finish(message.from_user.id) == 'no':
                
                if db.get_answerwin(message.from_user.id) == 'A':
                
# перезаписываем счетчик очков
                
                    score3 = int (db.get_scoreall(message.from_user.id)) + 1
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_scoreall(message.from_user.id, score3)
                    db.set_qusetioncount(message.from_user.id, questioncount)
                
                    await bot.send_message(message.from_user.id, "🟢Ты ответил правильно! 😃")
                    
                    
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
                    
# Отправляем вопрос и записываем правильный ответ в таблицу
                    else:
                        
                        questionanswer = await db.get_questionanswer(message.from_user.id)
                        questionanswer2 = questionanswer[0]
                
                        answerwin =  questionanswer2[0]
                        answerwinstr = str (answerwin)

                        db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                        await db.get_question(message)
                    
                else:
                    
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_qusetioncount(message.from_user.id, questioncount)
                                                               
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
                        
                    else:
                        if db.get_losercount(message.from_user.id) == 1:
                            losetext = str(await db.get_losetext(message.from_user.id))
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂" + "\n" + losetext, reply_markup=nav.mainMenu3)
                            questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                            db.set_qusetioncount(message.from_user.id, questioncount)
                        else:
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")

                            questionanswer = await db.get_questionanswer(message.from_user.id)
                            questionanswer2 = questionanswer[0]
                
                            answerwin =  questionanswer2[0]
                            answerwinstr = str (answerwin)

                            db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                            await db.get_question(message)

            else:
                userscoreall = db.get_scoreall(message.from_user.id)
                qcount = str(db.get_qcount(message.from_user.id))
                await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                if db.get_hr(message.from_user.id) == 1:
                    await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
        
        elif message.text == 'B':
            if db.get_finish(message.from_user.id) == 'no':
                
                if db.get_answerwin(message.from_user.id) == 'B':
                
# перезаписываем счетчик очков
                
                    score3 = int (db.get_scoreall(message.from_user.id)) + 1
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_scoreall(message.from_user.id, score3)
                    db.set_qusetioncount(message.from_user.id, questioncount)
                
                    await bot.send_message(message.from_user.id, "🟢Ты ответил правильно! 😃")
                    
                    
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
                    
# Отправляем вопрос и записываем правильный ответ в таблицу
                    else:
                        
                        questionanswer = await db.get_questionanswer(message.from_user.id)
                        questionanswer2 = questionanswer[0]
                
                        answerwin =  questionanswer2[0]
                        answerwinstr = str (answerwin)

                        db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                        await db.get_question(message)
                    
                else:
                                              
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_qusetioncount(message.from_user.id, questioncount)             
                                           
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
                        
                    else:
                       
                        if db.get_losercount(message.from_user.id) == 1:
                            losetext = str(await db.get_losetext(message.from_user.id))
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂" + "\n" + losetext, reply_markup=nav.mainMenu3)
                            questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                            db.set_qusetioncount(message.from_user.id, questioncount)
                        else:
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")

                            
                            questionanswer = await db.get_questionanswer(message.from_user.id)
                            questionanswer2 = questionanswer[0]
                
                            answerwin =  questionanswer2[0]
                            answerwinstr = str (answerwin)

                            db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                            await db.get_question(message)

            else:
                userscoreall = db.get_scoreall(message.from_user.id)
                qcount = str(db.get_qcount(message.from_user.id))
                await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                if db.get_hr(message.from_user.id) == 1:
                    await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
        
                
                
        elif message.text == 'C':
            if db.get_finish(message.from_user.id) == 'no':
                
                if db.get_answerwin(message.from_user.id) == 'C':
                
# перезаписываем счетчик очков
                
                    score3 = int (db.get_scoreall(message.from_user.id)) + 1
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_scoreall(message.from_user.id, score3)
                    db.set_qusetioncount(message.from_user.id, questioncount)
                
                    await bot.send_message(message.from_user.id, "🟢Ты ответил правильно! 😃")
                    
                    
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
                    
# Отправляем вопрос и записываем правильный ответ в таблицу
                    else:
                        
                        questionanswer = await db.get_questionanswer(message.from_user.id)
                        questionanswer2 = questionanswer[0]
                
                        answerwin =  questionanswer2[0]
                        answerwinstr = str (answerwin)

                        db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                        await db.get_question(message)
                    
                else:
                    
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_qusetioncount(message.from_user.id, questioncount)           
                                           
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
                        
                    else:
                        if db.get_losercount(message.from_user.id) == 1:
                            losetext = str(await db.get_losetext(message.from_user.id))
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂" + "\n" + losetext, reply_markup=nav.mainMenu3)
                            questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                            db.set_qusetioncount(message.from_user.id, questioncount)
                        else:
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")
                            
                            questionanswer = await db.get_questionanswer(message.from_user.id)
                            questionanswer2 = questionanswer[0]
                
                            answerwin =  questionanswer2[0]
                            answerwinstr = str (answerwin)

                            db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                            await db.get_question(message)

            else:
                userscoreall = db.get_scoreall(message.from_user.id)
                qcount = str(db.get_qcount(message.from_user.id))
                await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                if db.get_hr(message.from_user.id) == 1:
                    await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
        
        elif message.text == 'D':
            if db.get_finish(message.from_user.id) == 'no':
                
                if db.get_answerwin(message.from_user.id) == 'D':
                
# перезаписываем счетчик очков
                
                    score3 = int (db.get_scoreall(message.from_user.id)) + 1
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_scoreall(message.from_user.id, score3)
                    db.set_qusetioncount(message.from_user.id, questioncount)
                
                    await bot.send_message(message.from_user.id, "🟢Ты ответил правильно! 😃")
                    
                    
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
# Отправляем вопрос и записываем правильный ответ в таблицу
                    else:
                        
                        questionanswer = await db.get_questionanswer(message.from_user.id)
                        questionanswer2 = questionanswer[0]
                
                        answerwin =  questionanswer2[0]
                        answerwinstr = str (answerwin)

                        db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                        await db.get_question(message)
                    
                else:
                    
                    questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                    db.set_qusetioncount(message.from_user.id, questioncount)             
                                           
                    if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
                        
                    else:
                        if db.get_losercount(message.from_user.id) == 1:
                            losetext = str(await db.get_losetext(message.from_user.id))
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂" + "\n" + losetext, reply_markup=nav.mainMenu3)
                            questioncount = int (db.get_questioncount(message.from_user.id)) + 1
                            db.set_qusetioncount(message.from_user.id, questioncount)
                        else:
                            await bot.send_message(message.from_user.id, "🔴Ошибка, ты ответил не верно! 🙂")
                                                        
                            questionanswer = await db.get_questionanswer(message.from_user.id)
                            questionanswer2 = questionanswer[0]
                
                            answerwin =  questionanswer2[0]
                            answerwinstr = str (answerwin)

                            db.set_answerwinusers(message.from_user.id, answerwinstr)
                
                
                            await db.get_question(message)
                            
            else:
                userscoreall = db.get_scoreall(message.from_user.id)
                qcount = str(db.get_qcount(message.from_user.id))
                await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                if db.get_hr(message.from_user.id) == 1:
                    await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 
        
        
        elif message.text == '⬅️Назад':
            await bot.send_message(message.from_user.id, "Выбери, что хочешь сделать", reply_markup=nav.mainMenu)
            
        elif message.text == '😃Продолжить':

            if int (db.get_questioncount(message.from_user.id)) > db.get_qcount(message.from_user.id):
                        db.set_finish(message.from_user.id, "yes")
                        #leaderscore = db.get_leaderscore(message.from_user.id)
                        time2 = int(time.time()) - int(db.get_time1(message.from_user.id))
                        db.set_time2(message.from_user.id, time2)
                        userscoreall = db.get_scoreall(message.from_user.id)
                        qcount = str(db.get_qcount(message.from_user.id))
                        await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                        if db.get_hr(message.from_user.id) == 1:
                            await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link) 

            elif str (db.get_finish(message.from_user.id)) == "yes":
                leaderscore = db.get_leaderscore(message.from_user.id)
                userscoreall = db.get_scoreall(message.from_user.id)
                
                qcount = str(db.get_qcount(message.from_user.id))
                await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/" + qcount + " вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                if db.get_hr(message.from_user.id) == 1:
                    await bot.send_message(message.from_user.id, "И узнать больше о нашей компании", reply_markup=nav.link)    

            if int (db.get_questioncount(message.from_user.id)) == 1:
#общая статистика игр    
                stats1 = db.get_stats1(message.from_user.id)
                stats11 = int(stats1) + 1
    
                db.set_stats1(message.from_user.id, stats11)
            
# Отправляем вопрос и записываем правильный ответ в таблицу                
                questionanswer = await db.get_questionanswer(message.from_user.id)
                questionanswer2 = questionanswer[0]
                
                answerwin =  questionanswer2[0]
                answerwinstr = str (answerwin)

                db.set_answerwinusers(message.from_user.id, answerwinstr)

# Записываем время начала прохождения                 
                time1 = int(time.time())
                db.set_time1(message.from_user.id, time1)
                      
                await db.get_question(message)
            
            else:
                
                if str (db.get_finish(message.from_user.id)) == "yes":
                    pass
#                    leaderscore = db.get_leaderscore(message.from_user.id)
#                    userscoreall = db.get_scoreall(message.from_user.id)
               
#                    await bot.send_message(message.from_user.id, "Ты ответил правильно на " + userscoreall + "/32 вопросов!\n\nМожешь посмотреть таблицу 🏆Лидеров", reply_markup=nav.mainMenu)
                    
                else:
#общая статистика игр    
                    stats1 = db.get_stats1(message.from_user.id)
                    stats11 = int(stats1) + 1
    
                    db.set_stats1(message.from_user.id, stats11)
            
# Отправляем вопрос и записываем правильный ответ в таблицу                
                    questionanswer = await db.get_questionanswer(message.from_user.id)
                    questionanswer2 = questionanswer[0]
                
                    answerwin =  questionanswer2[0]
                    answerwinstr = str (answerwin)

                    db.set_answerwinusers(message.from_user.id, answerwinstr)
                      
                    await db.get_question(message)
        
#        elif message.text == '123456':
#            if db.get_token1(message.from_user.id) == '0':
#                db.set_token1(message.from_user.id, '1')
#                await message.answer_sticker(r'CAACAgIAAxkBAAEFWmti3Ad2j3mvMAnxmDSw8zsGxOG1mwACWxwAAtpy4Ur9VOsL46ZaqikE')
#                await bot.send_message(message.from_user.id, "Мррррр, твои золотые доспехи блестят на солнце. Теперь ты настоящий рыцарь, достойный кот своих родителей", reply_markup=nav.mainMenu) 
#            else:
#                await bot.send_message(message.from_user.id, "Вы уже использовали этот промокод!", reply_markup=nav.mainMenu)
                             
        else:
            if db.get_signup(message.from_user.id) == 'setnickname':
                if(len(message.text) > 25):
                    await bot.send_message(message.from_user.id, "Никнейм не должен превышать 25 символов")
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Ты ввел запрещённые символы")
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, "done")
                    db.set_learn(message.from_user.id, "done")
                    user_nickname = db.get_nickname(message.from_user.id)
#                    await bot.send_message(message.from_user.id, "Приятно познакомиться, " + user_nickname + "! " + "Напиши, сколько тебе лет?")
                    await bot.send_message(message.from_user.id, user_nickname + ", перед тобой викторина! Она посвящена Группе НЛМК.\n\nДля ответа на каждый вопрос дается 4 варианта ответа. Постарайся отвечать как можно быстрее.\n\nЗа каждый правильный ответ ты получаешь баллы.\n\nВ любой момент можешь посмотреть своё место в общей турнирной таблице среди всех участников.\n\nНу что, всё понятно? Тогда скорее нажимай 🟢Начать", reply_markup=nav.mainMenu)
            
#                    await bot.send_message(message.from_user.id, "Приятно познакомиться, " + user_nickname + "! " + ", перед тобой квиз-игра! Она посвящена Группе НЛМК.\n\nДля ответа на каждый вопрос дается 4 варианта ответа. Постарайся отвечать как можно быстрее.\n\nЗа каждый правильный ответ ты получаешь баллы.\n\nВ любой момент можешь посмотреть своё место в общей турнирной таблице среди всех участников.\n\nНу что, всё понятно? Тогда скорее нажимай ⚔️играть", reply_markup=nav.mainMenu)
            
#            elif db.get_signup(message.from_user.id) == 'setage':
 #               db.set_age(message.from_user.id, message.text)
  #              db.set_signup(message.from_user.id, "seteducation")
   #             await bot.send_message(message.from_user.id, "Понял, а где ты учишься?", reply_markup=nav.MenuEducation)
    #        
     #       elif db.get_signup(message.from_user.id) == 'seteducation':
      #              db.set_education(message.from_user.id, message.text)
       #             db.set_signup(message.from_user.id, "done")
        #            user_nickname = db.get_nickname(message.from_user.id)
         #           await bot.send_message(message.from_user.id, user_nickname + ", перед тобой викторина! Она посвящена Группе НЛМК.\n\nДля ответа на каждый вопрос дается 4 варианта ответа. Постарайся отвечать как можно быстрее.\n\nЗа каждый правильный ответ ты получаешь баллы.\n\nВ любой момент можешь посмотреть своё место в общей турнирной таблице среди всех участников.\n\nНу что, всё понятно? Тогда скорее нажимай 🟢Начать", reply_markup=nav.mainMenu)
            
            
            
            else:
                await bot.send_message(message.from_user.id, "Я ничего не понял. Воспользуйся клавиатурой", reply_markup=nav.mainMenu)



#@dp.callback_query_handler(text="btned1")
#async def bot_message(message: types.Message):
#    db.set_education(message.from_user.id, "ЛГТУ")
#    db.set_signup(message.from_user.id, "done")
#    await bot.send_message(message.from_user.id, "Перед тобой квиз-игра! Она посвящена Группе НЛМК.\n\nДля ответа на каждый вопрос дается 4 варианта ответа. Постарайся отвечать как можно быстрее.\n\nЗа каждый правильный ответ ты получаешь баллы.\n\nВ любой момент можешь посмотреть своё место в общей турнирной таблице среди всех участников.\n\nНу что, всё понятно? Тогда скорее нажимай ⚔️играть", reply_markup=nav.mainMenu)
            
#@dp.callback_query_handler(text="btned2")
#async def bot_message(message: types.Message):
#    db.set_education(message.from_user.id, "ЛМК")
#    db.set_signup(message.from_user.id, "done")
#    await bot.send_message(message.from_user.id, "Перед тобой квиз-игра! Она посвящена Группе НЛМК.\n\nДля ответа на каждый вопрос дается 4 варианта ответа. Постарайся отвечать как можно быстрее.\n\nЗа каждый правильный ответ ты получаешь баллы.\n\nВ любой момент можешь посмотреть своё место в общей турнирной таблице среди всех участников.\n\nНу что, всё понятно? Тогда скорее нажимай ⚔️играть", reply_markup=nav.mainMenu)
                        
#@dp.callback_query_handler(text="btned3")
#async def bot_message(message: types.Message):
#    db.set_education(message.from_user.id, "ЛКТиДХ")
#    db.set_signup(message.from_user.id, "done")
#    await bot.send_message(message.from_user.id, "Перед тобой квиз-игра! Она посвящена Группе НЛМК.\n\nДля ответа на каждый вопрос дается 4 варианта ответа. Постарайся отвечать как можно быстрее.\n\nЗа каждый правильный ответ ты получаешь баллы.\n\nВ любой момент можешь посмотреть своё место в общей турнирной таблице среди всех участников.\n\nНу что, всё понятно? Тогда скорее нажимай ⚔️играть", reply_markup=nav.mainMenu)

#@dp.callback_query_handler(text="btned4")
#async def bot_message(message: types.Message):
#    db.set_education(message.from_user.id, "Другой")
#    db.set_signup(message.from_user.id, "done")
#    await bot.send_message(message.from_user.id, "Перед тобой квиз-игра! Она посвящена Группе НЛМК.\n\nДля ответа на каждый вопрос дается 4 варианта ответа. Постарайся отвечать как можно быстрее.\n\nЗа каждый правильный ответ ты получаешь баллы.\n\nВ любой момент можешь посмотреть своё место в общей турнирной таблице среди всех участников.\n\nНу что, всё понятно? Тогда скорее нажимай ⚔️играть", reply_markup=nav.mainMenu)

@dp.callback_query_handler(text="btnLinkScore")
async def bot_message(message: types.Message):
    linkscore1 = int(db.get_statslinkscore(message.from_user.id))
    linkscore = linkscore1 + 1
    db.set_statslinkscore(message.from_user.id, linkscore)
    await bot.send_message(message.from_user.id, "https://lipetsk.hh.ru/employer/988387", reply_markup=nav.mainMenu)
                        
                
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)