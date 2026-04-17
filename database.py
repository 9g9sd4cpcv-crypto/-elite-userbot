import sqlite3

conn = sqlite3.connect("userbot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    messages INTEGER DEFAULT 0,
    xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    coins INTEGER DEFAULT 0
)
""")

def get_user(uid, name="User"):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (uid,))
    data = cursor.fetchone()

    if not data:
        cursor.execute("INSERT INTO users (user_id, username) VALUES (?,?)", (uid, name))
        conn.commit()
        return get_user(uid)

    return data

def update(uid, field, val):
    cursor.execute(f"UPDATE users SET {field}=? WHERE user_id=?", (val, uid))
    conn.commit()
