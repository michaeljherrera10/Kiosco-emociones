from flask import Flask, render_template, request
import csv
import os
from datetime import datetime

app = Flask(__name__, static_url_path='/static', static_folder='img')

CSV_FILE = 'registro_selecciones.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()

    now = datetime.now()
    fila = [
        now.strftime('%Y-%m-%d'),
        now.strftime('%H:%M:%S'),
        data.get('emocion', ''),
        data.get('principio', '')
    ]

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Fecha', 'Hora', 'Emoción', 'Principio'])
        writer.writerow(fila)

    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)