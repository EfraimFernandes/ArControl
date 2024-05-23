import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ArControl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ar TEXT NOT NULL,
    contato TEXT NOT NULL,
    s23 INTEGER NOT NULL,
    s24 INTEGER NOT NULL
)
''')

cursor.execute('''
INSERT INTO ArControl (ar, contato, s23, s24)
VALUES
    ('AR DANTAS E NASSERALA', 'JOSÉ', 1, 1),
    ('AR DAL CERTIFICADORA', 'FELICIANO', 1, 1),
    ('AR INTECH', 'CARLOS', 0, 1)
''')

conn.commit()
conn.close()

print("Banco de dados inicializado e populado com dados de exemplo.")
