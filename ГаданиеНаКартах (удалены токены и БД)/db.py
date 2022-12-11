import sqlite3
import random

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
        
        
        
    # Узнаем какая сейчас колода
    def get_deck(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT deck FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                deck = str(row[0])
            return deck
        
    # Узнаем какая cейчас категория
    def get_category(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT category FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                category = str(row[0])
            return category
        
        
    # Добавляем название колоды
    def set_deck(self, user_id, deck):
        with self.connection:
            return self.cursor.execute("UPDATE users SET deck = ? WHERE user_id = ?", (deck, user_id, ))
        
    # Добавляем название категории
    def set_category(self, user_id, category):
        with self.connection:
            return self.cursor.execute("UPDATE users SET category = ? WHERE user_id = ?", (category, user_id, ))  
    

    # Узнаем предсказание   
    def get_tarot(self, user_id):
        
        A = random.randint(1,78)

        with self.connection:
            return self.cursor.execute("SELECT cards.photo, cards.title, cards.text FROM cards, users WHERE users.user_id = ? AND cards.id = ? AND cards.deck = users.deck AND cards.category = users.category", (user_id, A, )).fetchall()

# Узнаем количество пользователей  
    def get_numberusers(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT COUNT (*) FROM users").fetchall()

    # Узнаем статистику 1
    def get_stats1(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT summ FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                deck = str(row[0])
            return deck

    # Узнаем статистику 2
    def get_stats2(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT work FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                deck = str(row[0])
            return deck

    # Узнаем статистику 3
    def get_stats3(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT love FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                deck = str(row[0])
            return deck
        
    # Узнаем статистику 4
    def get_stats4(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT persona FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                stats4 = str(row[0])
            return stats4

    # Узнаем статистику 5
    def get_stats5(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT rw FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                stats5 = str(row[0])
            return stats5

    # Узнаем статистику 6
    def get_stats6(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT dveri FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                stats6 = str(row[0])
            return stats6
        
    # Узнаем статистику 7
    def get_stats7(self, user_id):
        with self.connection:
            A = 1
            result = self.cursor.execute("SELECT tot FROM stats WHERE id = ?", (A,)).fetchall()
            for row in result:
                stats7 = str(row[0])
            return stats7
        
    # Узнаем статистику игрока
    def get_statsall(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT statsplayer FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                deck1 = str(row[0])
            return deck1
    
    # Добавляем статистику 1  
    def set_stats1(self, user_id, stats1):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET summ = ? WHERE id = ?", (stats1, A, )) 

    # Добавляем статистику 2  
    def set_stats2(self, user_id, stats2):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET work = ? WHERE id = ?", (stats2, A, ))  

    # Добавляем статистику 3
    def set_stats3(self, user_id, stats3):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET love = ? WHERE id = ?", (stats3, A, ))  
        
    # Добавляем статистику 4
    def set_stats4(self, user_id, stats4):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET persona = ? WHERE id = ?", (stats4, A, ))      

    # Добавляем статистику 5
    def set_stats5(self, user_id, stats5):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET rw = ? WHERE id = ?", (stats5, A, ))  

    # Добавляем статистику 6
    def set_stats6(self, user_id, stats6):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET dveri = ? WHERE id = ?", (stats6, A, )) 

    # Добавляем статистику 7
    def set_stats7(self, user_id, stats7):
        with self.connection:
            A = 1
            return self.cursor.execute("UPDATE stats SET tot = ? WHERE id = ?", (stats7, A, )) 

    # Добавляем статистику игрока
    def set_statsall(self, user_id, stats4):
        with self.connection:
            return self.cursor.execute("UPDATE users SET statsplayer = ? WHERE user_id = ?", (stats4, user_id, ))

        
    # Узнаем кто админ
    def get_admin(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT status FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                deck = str(row[0])
            return deck
    
    # Добавляем активного пользователя
    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id, ))
    

    # Узнаем активного пользователя
    def get_users(self, ):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()

        
        
        
        #with self.connection:
        #    result = self.cursor.execute("SELECT cards.photo, cards.title, cards.text FROM cards WHERE id = ? AND deck = ? AND category = ?", (A, B, C, )).fetchall()
        #    for row in result:
                
        #        return result
    
    
    
    # Закрытие соединения с базой данных    
    def close(self):
        self.conn.close()