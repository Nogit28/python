import sqlite3

conn = sqlite3.connect('floricultura.db')
cursor = conn.cursor()
sql = '''create table if not exists flores (
    codigo text primary key,
    desc text,
    unidade integer,
    quantidade integer,
    preco float
)'''
cursor.execute(sql)
conn.close()