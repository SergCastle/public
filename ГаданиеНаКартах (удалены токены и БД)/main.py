import logging
from subprocess import call
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink
import markups as nav
from db import Database

TOKEN = ''

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    print ('Бот вышел в онлайн')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Гадание на картах Таро считается одним из самых точных и правдивых методов поиска четких ответов на вопросы")
        await bot.send_message(message.from_user.id, "Пожалуйста, пользуйтесь главными правилами при работе с Таро:\n\n1. Перед гаданием поставьте четкий вопрос. Чем конкретнее будет запрос, тем конкретнее ответ\n\n2. Повторно гадать на одну и ту же ситуацию можно не ранее, чем через лунный месяц (29 дней)")
        await bot.send_message(message.from_user.id, "Можете начать гадать!", reply_markup = nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, "Можете начать гадать!", reply_markup = nav.mainMenu)

@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':

        await bot.send_message(message.from_user.id, "/stats - статистика \n/sendall - рассылка")

@dp.message_handler(commands=['stats'])
async def admin(message: types.Message):
    if db.get_admin(message.from_user.id) == 'admin':
        stats6 = int(db.get_stats1(message.from_user.id)) + int(db.get_stats2(message.from_user.id)) + int(db.get_stats3(message.from_user.id)) + int(db.get_stats4(message.from_user.id))
        stats8 = round(int(db.get_stats1(message.from_user.id))*100/stats6, 1)
        stats9 = round(int(db.get_stats2(message.from_user.id))*100/stats6, 1)
        stats10 = round(int(db.get_stats3(message.from_user.id))*100/stats6, 1)
        stats11 = round(int(db.get_stats4(message.from_user.id))*100/stats6, 1)
        stats1 = "\n\nОбщий: " + db.get_stats1(message.from_user.id) + " [" + str(stats8) + "%]"
        stats2 = "\nРабота: " + db.get_stats2(message.from_user.id) + " [" + str(stats9) + "%]"
        stats3 = "\nЛюбовь: " + db.get_stats3(message.from_user.id) + " [" + str(stats10) + "%]"
        stats4 = "\nЛичность: " + db.get_stats4(message.from_user.id) + " [" + str(stats11) + "%]"
        statsnumberusers = db.get_numberusers(message.from_user.id)
        statsnumberusers2 = str(statsnumberusers[0][0])
        stats5 = "-----------------------------------\nПользователей: " + statsnumberusers2
        
        stats7 = "\n-----------------------------------\nГаданий: " + str(stats6)
        
        stats12 = int(db.get_stats5(message.from_user.id)) + int(db.get_stats6(message.from_user.id)) + int(db.get_stats7(message.from_user.id))
        stats13 = round(int(db.get_stats5(message.from_user.id))*100/stats12, 1)
        stats14 = round(int(db.get_stats6(message.from_user.id))*100/stats12, 1)
        stats15 = round(int(db.get_stats7(message.from_user.id))*100/stats12, 1)
        
        stats16 = "\n-----------------------------------\nРейдер Уайт: " + db.get_stats5(message.from_user.id) + " [" + str(stats13) + "%]"
        stats17 = "\n78 дверей: " + db.get_stats6(message.from_user.id) + " [" + str(stats14) + "%]"
        stats18 = "\nТот: " + db.get_stats7(message.from_user.id) + " [" + str(stats15) + "%]"
        
        await bot.send_message(message.from_user.id, stats5 + stats7 + stats1 + stats2 + stats3 + stats4 + stats16 + stats17 + stats18)
    


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

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Гадать':
            
            await bot.send_message(message.from_user.id, "Мысленно сформулируйте свой вопрос и выберите его категорию", reply_markup = nav.category)

        elif message.text == 'Профиль':
            user_deck = "Колода: " + db.get_deck(message.from_user.id)
            user_category = "\nКатегория: " + db.get_category(message.from_user.id)
            user_tarot = "\nКол-во гаданий: " + db.get_statsall(message.from_user.id)
            await bot.send_message(message.from_user.id, user_deck + user_category + user_tarot, reply_markup = nav.mainMenu)
            
        elif message.text == 'Колода':

            await bot.send_message(message.from_user.id, "Выбери колоду", reply_markup = nav.deck)

        elif message.text == 'Помощь':
            text = hlink('нашей группы','https://t.me/oldtaro_bot_admin')
            text2 = hlink('QIWI','qiwi.com/n/CIPIR746')
            await bot.send_message(message.from_user.id, "Если вы заметили ошибку или у вас есть вопросы и предложения, напишите их в комментариях " + text + "\n\nЕсли хотите поддержать проект материально, ссылка на " + text2, reply_markup = nav.mainMenu, parse_mode="HTML")           
        
        else:
            await bot.send_message(message.from_user.id, "Пожалуйста, используйте меню навигации", reply_markup = nav.mainMenu)



@dp.callback_query_handler(text="btnAll")
async def deletemarkups(call: types.CallbackQuery):
    db.set_category(call.from_user.id, 'Общая' )

#общая статистика игрока    
    statsplayer1 = db.get_statsall(call.from_user.id)
    statsplayer11 = int(statsplayer1) + 1
    
    db.set_statsall(call.from_user.id, statsplayer11)

#общая статистика    
    stats1 = db.get_stats1(call.from_user.id)
    stats11 = int(stats1) + 1
    
    db.set_stats1(call.from_user.id, stats11)

    tarotall0 = db.get_tarot(call.from_user.id)
    tarotall = tarotall0[0]
    photo = tarotall[0]
    title = tarotall[1]
    text = "\n\n" + tarotall[2]
    
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_sticker(call.from_user.id, sticker = photo)
    await bot.send_message(call.from_user.id, title + text, reply_markup = nav.mainMenu)

@dp.callback_query_handler(text="btnWork")
async def deletemarkups(call: types.CallbackQuery):
    db.set_category(call.from_user.id, 'Работа' )

#общая статистика игрока    
    statsplayer1 = db.get_statsall(call.from_user.id)
    statsplayer11 = int(statsplayer1) + 1
    
    db.set_statsall(call.from_user.id, statsplayer11)

#общая статистика 
    stats1 = db.get_stats2(call.from_user.id)
    stats11 = int(stats1) + 1
    
    db.set_stats2(call.from_user.id, stats11)

    tarotall0 = db.get_tarot(call.from_user.id)
    tarotall = tarotall0[0]
    photo = tarotall[0]
    title = tarotall[1]
    text = "\n\n" + tarotall[2]
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_sticker(call.from_user.id, sticker = photo)
    await bot.send_message(call.from_user.id, title + text, reply_markup = nav.mainMenu)

@dp.callback_query_handler(text="btnLove")
async def deletemarkups(call: types.CallbackQuery):
    db.set_category(call.from_user.id, 'Любовь' )

#общая статистика игрока    
    statsplayer1 = db.get_statsall(call.from_user.id)
    statsplayer11 = int(statsplayer1) + 1
    
    db.set_statsall(call.from_user.id, statsplayer11)

#общая статистика 
    stats1 = db.get_stats3(call.from_user.id)
    stats11 = int(stats1) + 1
    
    db.set_stats3(call.from_user.id, stats11)

    tarotall0 = db.get_tarot(call.from_user.id)
    tarotall = tarotall0[0]
    photo = tarotall[0]
    title = tarotall[1]
    text = "\n\n" + tarotall[2]
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_sticker(call.from_user.id, sticker = photo)
    await bot.send_message(call.from_user.id, title + text, reply_markup = nav.mainMenu)

@dp.callback_query_handler(text="btnPersona")
async def deletemarkups(call: types.CallbackQuery):
    db.set_category(call.from_user.id, 'Личность' )

#общая статистика игрока    
    statsplayer1 = db.get_statsall(call.from_user.id)
    statsplayer11 = int(statsplayer1) + 1
    
    db.set_statsall(call.from_user.id, statsplayer11)

#общая статистика 
    stats1 = db.get_stats4(call.from_user.id)
    stats11 = int(stats1) + 1
    
    db.set_stats4(call.from_user.id, stats11)

    tarotall0 = db.get_tarot(call.from_user.id)
    tarotall = tarotall0[0]
    photo = tarotall[0]
    title = tarotall[1]
    text = "\n\n" + tarotall[2]
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_sticker(call.from_user.id, sticker = photo)
    await bot.send_message(call.from_user.id, title + text, reply_markup = nav.mainMenu)


@dp.callback_query_handler(text="btnRayder")
async def deletemarkups(call: types.CallbackQuery):
    db.set_deck(call.from_user.id, 'Рейдер_Уайт' )
    
    #общая статистика    
    stats1 = db.get_stats5(call.from_user.id)
    stats11 = int(stats1) + 1
    
    db.set_stats5(call.from_user.id, stats11)
    
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, "Колода изменена", reply_markup = nav.mainMenu)

@dp.callback_query_handler(text="btnDoor")
async def deletemarkups(call: types.CallbackQuery):
    db.set_deck(call.from_user.id, '78_дверей' )
    
    #общая статистика    
    stats1 = db.get_stats6(call.from_user.id)
    stats11 = int(stats1) + 1
    
    db.set_stats6(call.from_user.id, stats11)
    
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, "Колода изменена", reply_markup = nav.mainMenu)
    
@dp.callback_query_handler(text="btnTot")
async def deletemarkups(call: types.CallbackQuery):
    db.set_deck(call.from_user.id, 'Тот' )
    
    #общая статистика    
    stats1 = db.get_stats7(call.from_user.id)
    stats11 = int(stats1) + 1
    
    db.set_stats7(call.from_user.id, stats11)
    
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, "Колода изменена", reply_markup = nav.mainMenu)
    
    
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
