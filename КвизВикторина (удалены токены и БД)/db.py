import sqlite3
import random
import markups as nav
import time
import datetime

from create_bot import bot

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()      
       
    # Добавление нового пользователя
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        
    # Проверяем существуетли пользователь в базе   
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))
        
    # Добавляем никнейм
    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE users SET nickname = ? WHERE user_id = ?", (nickname, user_id, ))

    # Добавляем возраст
    def set_age(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id, ))

    # Добавляем образование
    def set_education(self, user_id, education):
        with self.connection:
            return self.cursor.execute("UPDATE users SET education = ? WHERE user_id = ?", (education, user_id, ))

    # Добавляем финиш игры
    def set_finish(self, user_id, finish):
        with self.connection:
            return self.cursor.execute("UPDATE users SET finish = ? WHERE user_id = ?", (finish, user_id, ))


    # Узнаем финиш игры
    def get_finish(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT finish FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                finish = str (row[0])
                return finish


    # Узнаем статус регистрации
    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str (row[0])
                return signup

    # Узнаем кто админ
    def get_admin(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT admin FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                admin = str(row[0])
            return admin

    # Узнаем статистику 1
    def get_stats1(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT play FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                play = str(row[0])
            return play

    # Узнаем кол-во вопросов
    def get_qcount(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT qcount FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                qcount = int(row[0])
            return qcount

    # Узнаем кол-во лидеров
    def get_lcount(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT lcount FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                lcount = int(row[0])
            return lcount

    # Узнаем ссылку
    def get_hr(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT hr FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                hr = int(row[0])
            return hr

    # Узнаем проигрыш
    def get_lose(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT lose FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                lose = int(row[0])
            return lose
    # Добавляем кол-вопросов 
    def set_qcount(self, user_id, qcount):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET qcount = ? WHERE id = ?", (qcount, A, )) 

    # Добавляем ссылку
    def set_hr(self, user_id, qcount):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET hr = ? WHERE id = ?", (qcount, A, )) 

    # Добавляем обяснения
    def set_lose(self, user_id, qcount):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET lose = ? WHERE id = ?", (qcount, A, )) 

    # Добавляем кол-лидеров
    def set_lcount(self, user_id, lcount):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET lcount = ? WHERE id = ?", (lcount, A, )) 

    # Узнаем нужен ответ на вопрос или нет
    def get_losercount(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT lose FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                lose = int(row[0])
            return lose

    # Добавляем статистику 1  
    def set_stats1(self, user_id, stats1):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET play = ? WHERE id = ?", (stats1, A, ))

    # Узнаем статистику 2
    def get_statslinkscore(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT linkscore FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                linkscore = str(row[0])
            return linkscore

    # Добавляем статистику 1  
    def set_statslinkscore(self, user_id, statslink):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET linkscore = ? WHERE id = ?", (statslink, A, )) 

    # Узнаем количество пользователей  
    def get_numberusers(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT COUNT (*) FROM users").fetchall()

    # Узнаем количество пользователей  
    def get_numberusers2(self, user_id):
        with self.connection:
            A = "ЛГТУ"
            return self.cursor.execute("SELECT COUNT (*) FROM users WHERE users.education = ?", (A,)).fetchall()

    # Узнаем количество пользователей  
    def get_numberusers3(self, user_id):
        with self.connection:
            A = "ЛМК"
            return self.cursor.execute("SELECT COUNT (*) FROM users WHERE users.education = ?", (A,)).fetchall()

    # Узнаем количество пользователей  
    def get_numberusers4(self, user_id):
        with self.connection:
            A = "ЛКТиДХ"
            return self.cursor.execute("SELECT COUNT (*) FROM users WHERE users.education = ?", (A,)).fetchall()

    # Узнаем количество пользователей  
    def get_numberusers5(self, user_id):
        with self.connection:
            A = "Другой"
            return self.cursor.execute("SELECT COUNT (*) FROM users WHERE users.education = ?", (A,)).fetchall()
    
    # Добавляем этап регистрации
    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id, ))

    # Узнаем статус регистрации
    def get_nickname(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT nickname FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                nickname = str (row[0])
                return nickname

    # Узнаем айди игрока
    def get_idplayer(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                idplayer = str (row[0])
                return idplayer
    
    # Узнаем кол-во очков (опыт)
    def get_score(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT score FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                score = str (row[0])
                return score
    
    # Узнаем кол-во очков всего
    def get_scoreall(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT scoreall FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                scoreall = str (row[0])
                return scoreall
    
      
    
    # Узнаем счетчик вопросов
    def get_questioncount(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT questioncount FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                win = str (row[0])
                return win

    # Добавляем счетчик вопросов
    def set_qusetioncount(self, user_id, learn):
        with self.connection:
            return self.cursor.execute("UPDATE users SET questioncount = ? WHERE user_id = ?", (learn, user_id, ))


    # Узнаем обучение
    def get_learn(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT learn FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                learn = str (row[0])
                return learn 
    
    # Добавляем обучение
    def set_learn(self, user_id, learn):
        with self.connection:
            return self.cursor.execute("UPDATE users SET learn = ? WHERE user_id = ?", (learn, user_id, ))
        
    # Стать админом
    def set_admin(self, user_id, admin):
        with self.connection:
            return self.cursor.execute("UPDATE users SET admin = ? WHERE user_id = ?", (admin, user_id, ))   

    # Сбросить свою регистрацию
    def set_reset(self, user_id, reset):
        with self.connection:
            return self.cursor.execute("UPDATE users SET user_id = ? WHERE user_id = ?", (reset, user_id, ))
    
    # Узнаем активного пользователя
    def get_users(self, ):
        with self.connection:
            A = 5
            return self.cursor.execute("SELECT user_id, active FROM users WHERE user_id > ?", (A, )).fetchall()

    # Узнаем пользователя 2
    def get_usersnew(self, ):
        with self.connection:
            B = "yes"
            С = 5
            return self.cursor.execute("SELECT user_id, active FROM users WHERE reset = ? AND user_id > ?", (B,С )).fetchall()

    # Добавляем активного пользователя
    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id, ))
    
# Добавляем вопрос и ответы в таблицу юзеров ___________________________________________________________________________________
            
    # Добавляем ответ правильный вопроса в таблицу юзеров
    def set_answerwinusers(self, user_id, answerwinusers):
        with self.connection:
            return self.cursor.execute("UPDATE users SET answerwin = ? WHERE user_id = ?", (answerwinusers, user_id, ))  
        
    # Добавляем опыт игроку
    def set_score(self, user_id, setscore):
        with self.connection:
            return self.cursor.execute("UPDATE users SET score = ? WHERE user_id = ?", (setscore, user_id, ))     

    # Добавляем общий счет игроку
    def set_scoreall(self, user_id, setscore):
        with self.connection:
            return self.cursor.execute("UPDATE users SET scoreall = ? WHERE user_id = ?", (setscore, user_id, )) 
    
    
# Узнаем тексты вопросов и ответов из таблицы юзеров___________________________________________________________________________
            
    # Узнаем ответ правильный
    def get_answerwin(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT answerwin FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                answerwin = str (row[0])
                return answerwin


            
    # Узнаем уровень героя
    def get_lvl(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT lvl FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                answerwin = str (row[0])
                return answerwin
            
    # Добавляем уровень героя
    def set_lvl(self, user_id, setscore):
        with self.connection:
            return self.cursor.execute("UPDATE users SET lvl = ? WHERE user_id = ?", (setscore, user_id, ))    

    # Добавляем время начала прохождения
    def set_time1(self, user_id, time1):
        with self.connection:
            return self.cursor.execute("UPDATE users SET time1 = ? WHERE user_id = ?", (time1, user_id, )) 

    # Добавляем время окончания прохождения
    def set_time2(self, user_id, time2):
        with self.connection:
            return self.cursor.execute("UPDATE users SET time2 = ? WHERE user_id = ?", (time2, user_id, )) 

    # Узнаем время начала прохождения
    def get_time1(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT time1 FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                time1 = int (row[0])
                return time1 

    # Узнаем время окончания прохождения
    def get_time2(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT time2 FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                time2 = int (row[0])
                return time2 


        
# Токены ____________________________________________________________________________ 
       
    # Узнаем токен1
    def get_token1(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT token1 FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                token1 = str (row[0])
                return token1                

    # Добавляем уровень героя
    def set_token1(self, user_id, settoken1):
        with self.connection:
            return self.cursor.execute("UPDATE users SET token1 = ? WHERE user_id = ?", (settoken1, user_id, ))                

    # Узнаем лидеров по количеству очков
    def get_leaderscore(self, user_id):
        with self.connection:
            A = "no"
            return self.cursor.execute("SELECT users.nickname, users.scoreall, users.id, users.time2 FROM users WHERE users.admin = ? ORDER BY users.scoreall DESC, users.time2 ASC", (A, )).fetchall()

    # Узнаем лидеров по количеству очков
    
    def get_leaderscore100(self, user_id):
        with self.connection:
            A = "no"
            result = self.cursor.execute("SELECT users.nickname, users.scoreall, users.id, users.time2 FROM users WHERE users.admin = ? ORDER BY users.scoreall DESC, users.time2 ASC", (A, )).fetchall()
            for row in result:
                leaderscore = "\n1. " + str (result[0][0]) + " #" + str (result[0][2]) + " - " + str (result[0][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[0][3]))) + ")\
                    \n2. " + str (result[1][0]) + " #" + str (result[1][2]) + " - " + str (result[1][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[1][3]))) + ")\
                        \n3. " + str (result[2][0]) + " #" + str (result[2][2]) + " - " + str (result[2][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[2][3]))) + ")\
                            \n4. " + str (result[3][0]) + " #" + str (result[3][2]) + " - " + str (result[3][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[3][3]))) + ")\
                                \n5. " + str (result[4][0]) + " #" + str (result[4][2]) + " - " + str (result[4][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[4][3]))) + ")\
                                    \n6. " + str (result[5][0]) + " #" + str (result[5][2]) + " - " + str (result[5][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[5][3]))) + ")\
                                        \n7. " + str (result[6][0]) + " #" + str (result[6][2]) + " - " + str (result[6][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[6][3]))) + ")\
                                            \n8. " + str (result[7][0]) + " #" + str (result[7][2]) + " - " + str (result[7][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[7][3]))) + ")\
                                                \n9. " + str (result[8][0]) + " #" + str (result[8][2]) + " - " + str (result[8][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[8][3]))) + ")\
                                                    \n10. " + str (result[9][0]) + " #" + str (result[9][2]) + " - " + str (result[9][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[9][3]))) + ")"
                                                        
                                                                    
                                                                    
                return leaderscore 

    


    # Узнаем лидеров ЛГТУ по количеству очков
    def get_leaderscore1(self, user_id):
        with self.connection:
            A = "ЛГТУ"
            result = self.cursor.execute("SELECT users.nickname, users.scoreall, users.id, users.time2 FROM users WHERE users.education = ? ORDER BY users.scoreall DESC, users.time2 ASC", (A, )).fetchall()
            for row in result:
                leaderscore1 = "\n1. " + str (result[0][0]) + " #" + str (result[0][2]) + " - " + str (result[0][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[0][3]))) + ")\
                    \n2. " + str (result[1][0]) + " #" + str (result[1][2]) + " - " + str (result[1][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[1][3]))) + ")\
                        \n3. " + str (result[2][0]) + " #" + str (result[2][2]) + " - " + str (result[2][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[2][3]))) + ")"
                                                       
                return leaderscore1


    # Узнаем лидеров ЛМК по количеству очков
    def get_leaderscore2(self, user_id):
        with self.connection:
            A = "ЛМК"
            result = self.cursor.execute("SELECT users.nickname, users.scoreall, users.id, users.time2 FROM users WHERE users.education = ? ORDER BY users.scoreall DESC, users.time2 ASC", (A, )).fetchall()
            for row in result:
                leaderscore2 = "\n1. " + str (result[0][0]) + " #" + str (result[0][2]) + " - " + str (result[0][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[0][3]))) + ")\
                    \n2. " + str (result[1][0]) + " #" + str (result[1][2]) + " - " + str (result[1][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[1][3]))) + ")\
                        \n3. " + str (result[2][0]) + " #" + str (result[2][2]) + " - " + str (result[2][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[2][3]))) + ")"
                                                       
                return leaderscore2   

    # Узнаем лидеров ЛГТУ по количеству очков
    def get_leaderscore3(self, user_id):
        with self.connection:
            A = "ЛКТиДХ"
            result = self.cursor.execute("SELECT users.nickname, users.scoreall, users.id, users.time2 FROM users WHERE users.education = ? ORDER BY users.scoreall DESC, users.time2 ASC", (A, )).fetchall()
            for row in result:
                A = "ЛКТиДХ"
                leaderscore3 = "\n1. " + str (result[0][0]) + " #" + str (result[0][2]) + " - " + str (result[0][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[0][3]))) + ")\
                    \n2. " + str (result[1][0]) + " #" + str (result[1][2]) + " - " + str (result[1][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[1][3]))) + ")\
                        \n3. " + str (result[2][0]) + " #" + str (result[2][2]) + " - " + str (result[2][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[2][3]))) + ")"
                                                       
                return leaderscore3

    # Узнаем лидеров ЛГТУ по количеству очков
    def get_leaderscore4(self, user_id):
        with self.connection:
            A = "Другой"
            result = self.cursor.execute("SELECT users.nickname, users.scoreall, users.id, users.time2 FROM users WHERE users.education = ? ORDER BY users.scoreall DESC, users.time2 ASC", (A, )).fetchall()
            for row in result:
                leaderscore4 = "\n1. " + str (result[0][0]) + " #" + str (result[0][2]) + " - " + str (result[0][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[0][3]))) + ")\
                    \n2. " + str (result[1][0]) + " #" + str (result[1][2]) + " - " + str (result[1][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[1][3]))) + ")\
                        \n3. " + str (result[2][0]) + " #" + str (result[2][2]) + " - " + str (result[2][1]) + "/32 (" + str(datetime.timedelta(seconds = (result[2][3]))) + ")"
                                                       
                return leaderscore4


    # Узнаем ответ правильный
    def get_education(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT education FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                education = str (row[0])
                return education

   
    # Добавляем ответ игрока
    def set_answerwin(self, user_id, answerwin):
        with self.connection:
            return self.cursor.execute("UPDATE users SET answerwin = ? WHERE user_id = ?", (answerwin, user_id, ))
   
   
 
 
 
# Аватарки котов ____________________________________________________________________________


    # Узнаем аватарку король кот
    async def get_royalcat(self, message):
 
        A = 1
        
        for ret in self.cursor.execute("SELECT cats.photo FROM cats WHERE id = ?", (A, )).fetchall():
            await bot.send_photo(message.from_user.id, ret[0])  


    # Узнаем аватарку воин кот
    async def get_warcat(self, message):
 
        A = 2
        
        for ret in self.cursor.execute("SELECT cats.photo FROM cats WHERE id = ?", (A, )).fetchall():
            await bot.send_photo(message.from_user.id, ret[0])


    # Узнаем аватарку маг кот
    async def get_magcat(self, message):
 
        A = 3
        
        for ret in self.cursor.execute("SELECT cats.photo FROM cats WHERE id = ?", (A, )).fetchall():
            await bot.send_photo(message.from_user.id, ret[0])


    # Узнаем аватарку обычная
    async def get_defcat(self, message):
 
        A = 0
        
        for ret in self.cursor.execute("SELECT cats.photo FROM cats WHERE id = ?", (A, )).fetchall():
            await bot.send_photo(message.from_user.id, ret[0])
   
   
    # Выбираем вопрос из таблицы
    async def get_questionanswer(self, user_id):
        
        with self.connection:
            result = self.cursor.execute("SELECT question.answerwin FROM question, users WHERE users.user_id = ? AND question.id = users.questioncount", (user_id, )).fetchall()
            for row in result:
                textanswerwin = str (row[0])
                return textanswerwin

    # Выбираем текст пояснения при ошибке
    async def get_losetext(self, user_id):
        
        with self.connection:
            result = self.cursor.execute("SELECT question.losetext FROM question, users WHERE users.user_id = ? AND question.id = users.questioncount", (user_id, )).fetchall()
            for row in result:
                losetext = str (row[0])
                return losetext        

    # Узнаем вопрос и текст (update)  
    async def get_question(self, message):
        
        A = message.from_user.id
        
        for ret in self.cursor.execute("SELECT question.photo, question.text, question.answer1, question.answer2, question.answer3, question.answer4, question.answerwin FROM question, users WHERE users.user_id = ? AND question.id = users.questioncount", (A, )).fetchall():
            await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[1]}\n\nA) {ret[2]}\nB) {ret[3]}\nC) {ret[4]}\nD) {ret[5]}', reply_markup=nav.mainMenu2)

   
    # Выбираем вопрос из таблицы
    def get_questionanswerone(self, user_id):
        
        A = 1
        
        with self.connection:
            result = self.cursor.execute("SELECT question.photo, question.text, question.answer1, question.answer2, question.answer3, question.answer4, question.answerwin, question.id FROM question WHERE id = ?", (A, )).fetchall()
            for row in result:
                return result 
         

    # Закрытие соединения с базой данных    
    def close(self):
        self.conn.close()
        

        
        