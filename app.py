from flask import Flask, request, render_template, redirect
from flask_mysqldb import MySQL
import config
import json

app = Flask(__name__)
mysql = MySQL(app)


@app.route('/')
def index():
    db_conn = config.db_connection()
    cur = db_conn.cursor()
    # retrieve data from the database
    cur.execute('SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 1')
    latest_data = cur.fetchone()

    cur.execute('SELECT * FROM plant_data')
    plant_data = cur.fetchall()

    cur.close()

    return render_template('index.html', latest_data=latest_data, plant_data=plant_data)


@app.route('/new_plant', methods=['POST'])
def new_plant():
    # retrieve input from form
    name = request.form['plantName']
    temp = request.form['temperature']
    hum = request.form['humidity']
    mois = request.form['moisture']

    db_conn = config.db_connection()
    cur = db_conn.cursor()
    # insert query to the database
    add_query = f'INSERT INTO plant_data (plant_name, temperature, humidity, moisture) VALUES {name, temp, hum, mois}'
    cur.execute(add_query)
    db_conn.commit()
    cur.close()
    db_conn.close()

    return redirect('/')


@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.get_json()
    # obtain data from the hardware device
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
    # app.run(debug=True)
