from flask import Flask, request
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

# MySQL database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sensor'

mysql = MySQL(app)


@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.get_json()

    temperature = data['temperature']
    humidity = data['humidity']
    pressure = data['pressure']
    moisture = data['moisture']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO sensor_data (temperature, humidity, pressure, moisture) VALUES (%s, %s, %s, %s)",
                (temperature, humidity, pressure, moisture))
    mysql.connection.commit()
    cur.close()

    return 'Data inserted successfully!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
