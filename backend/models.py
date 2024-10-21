import sqlite3

def create_weather_table():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY
        city TEXT NOT NULL,
        temperature TEXT NOT NULL,
        condition TEXT NOT NULL
        )'''
    )
    conn.commit()
    conn.close()

