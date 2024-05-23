from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Função para obter dados do banco de dados
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ar, contato, s23, s24 FROM ArControl")
    rows = cursor.fetchall()
    conn.close()
    # Calcular status com base em s23 e s24
    data = [(row[0], row[1], 'Renovado' if row[2] == 1 and row[3] == 1 else 'Cancelado' if row[2] == 1 and row[3] == 0 else 'Contratado') for row in rows]
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)