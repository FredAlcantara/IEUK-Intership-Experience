from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import config
import json

app = Flask(__name__)
mysql = MySQL(app)


@app.route('/')
def index():
    db_conn = config.db_connection()
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 1")
    latest_data = cur.fetchone()
    cur.close()

    return render_template('index.html', latest_data=latest_data)


@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.get_json()

    temperature = data['temperature']
    humidity = data['humidity']
    pressure = data['pressure']
    moisture = data['moisture']

    db_conn = config.db_connection()
    cur = db_conn.cursor()
    cur.execute("INSERT INTO sensor_data (temperature, humidity, pressure, moisture) VALUES (%s, %s, %s, %s)",
                (temperature, humidity, pressure, moisture))
    db_conn.commit()
    cur.close()

    return 'Data inserted successfully!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
