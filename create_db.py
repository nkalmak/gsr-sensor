import sqlite3

connection = sqlite3.connect('gsr.db')


with open('schema.sql', encoding='utf-8') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO gsr values(datetime('now', 'localtime'), 35)")

connection.commit()
connection.close()