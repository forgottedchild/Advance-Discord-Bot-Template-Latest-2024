import sqlite3

class Database:
    def __init__(self, db_path="data/database.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        # Example table for user data
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                               user_id INTEGER PRIMARY KEY,
                               coins INTEGER DEFAULT 0)""")
        self.conn.commit()

    def get_coins(self, user_id):
        self.cursor.execute("SELECT coins FROM users WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def add_coins(self, user_id, amount):
        coins = self.get_coins(user_id) + amount
        self.cursor.execute("REPLACE INTO users (user_id, coins) VALUES (?, ?)", (user_id, coins))
        self.conn.commit()

    def close(self):
        self.conn.close()
