import sqlite3
from sqlite3 import Error
import os

class DatabaseManager:
    def __init__(self, db_file):
        """Initialize the database manager with the database file."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(self):
        """Create the messages table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            source_message_id TEXT NOT NULL,
            user_id TEXT NOT NULL,
            user_name TEXT NOT NULL,
            message_text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            answered INTEGER DEFAULT 0
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_message(self, source, source_message_id, user_id, user_name, message_text):
        """Insert a new message into the messages table."""
        sql = '''INSERT INTO messages(source, source_message_id, user_id, user_name, message_text)
                 VALUES(?,?,?,?,?)'''
        cur = self.connection.cursor()
        cur.execute(sql, (source, source_message_id, user_id, user_name, message_text))
        self.connection.commit()
        return cur.lastrowid

    def get_unanswered_messages(self):
        """Fetch all unanswered messages."""
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM messages WHERE answered = 0")
        return cur.fetchall()

    def mark_message_as_answered(self, message_id):
        """Mark a message as answered."""
        sql = '''UPDATE messages SET answered = 1 WHERE id = ?'''
        cur = self.connection.cursor()
        cur.execute(sql, (message_id,))
        self.connection.commit()