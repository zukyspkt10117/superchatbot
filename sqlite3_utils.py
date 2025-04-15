import sqlite3
from configuration import DB_PATH
from datetime import datetime

# --- Helper database functions ---
def get_connection():
    return sqlite3.connect(DB_PATH)

def get_user_by_chat_id(chat_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT chat_id, name, state FROM users WHERE chat_id = ?", (chat_id,))
        row = cursor.fetchone()
        if row:
            return {'chat_id': row[0], 'name': row[1], 'state': row[2]}
        return None

def create_user(chat_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (chat_id, state, registered_at) VALUES (?, 'Init', ?)",
                       (chat_id, datetime.now()))
        conn.commit()

def update_user_name(chat_id, name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ? WHERE chat_id = ?", (name, chat_id))
        conn.commit()

def update_user_state(chat_id, new_state):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET state = ? WHERE chat_id = ?", (new_state, chat_id))
        conn.commit()