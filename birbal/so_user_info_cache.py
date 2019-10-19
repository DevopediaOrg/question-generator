import sqlite3
import json

class SqliteHandler:
    def __init__(self, path, logger):
        self.logger = logger
        self.logger.debug("Connecting the table %s", path)
        self.db = sqlite3.connect(path)
        self.cu = self.db.cursor()
        self.create_table()

    def create_table(self):
        self.cu.execute('''
        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, updated_at BIGINT, userdata TEXT,
        userid BIGINT)''')
        self.db.commit()
        
    def insert_user(self, time, userid, userdata):
        self.cu.execute('''INSERT INTO users(updated_at, userdata, userid)
                  VALUES(?,?,?)''', (time, json.dumps(userdata), userid))
        self.db.commit()

    def get_user(self, userid):
        try:
            self.cu.execute("SELECT userid, updated_at, userdata FROM users where userid=?", (userid,))
            rows = self.cu.fetchone()
            if rows:
                return list(rows)
        except Exception as e:
            self.logger("Error while getting data from db", e)
        return []
