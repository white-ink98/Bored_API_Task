import sqlite3

class ActivityDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity TEXT,
                type TEXT,
                participants INTEGER,
                price REAL,
                accessibility REAL
            )
        ''')
        self.conn.commit()

    def save_activity(self, activity_data):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO activities (activity, type, participants, price, accessibility)
            VALUES (?, ?, ?, ?, ?)
        ''', (activity_data['activity'], activity_data['type'], activity_data['participants'], activity_data['price'], activity_data['accessibility']))
        self.conn.commit()

    def get_latest_activities(self, limit=5):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM activities
            ORDER BY id DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()
