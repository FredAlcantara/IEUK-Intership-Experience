from machine import I2C, Pin, ADC
from bme280 import BME280
import urequests
import ujson
import time

# Server configuration
server_url = 'http://192.168.1.97:5000/insert_data'

# Initialize BME280 sensor
i2c = I2C(0)
bme = BME280(i2c=i2c)

# Initialize soil moisture sensor
sm_sensor = ADC(Pin(26))

# Calibrated values for soil moisture sensor
sensor_min = 10000  # Replace with your "dry" value
sensor_max = 50000  # Replace with your "wet" value

while True:
    # Read BME280 sensor data
    temperature = bme.values[0]
    humidity = bme.values[2]
    pressure = bme.values[1]

    # Read soil moisture sensor data
    raw_value = sm_sensor.read_u16()
    moisture_percentage = (sensor_max - raw_value) / \
        (sensor_max - sensor_min) * 100

    # Prepare the data payload
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'moisture': moisture_percentage
    }

    # Send the data to the server
    response = urequests.post(server_url, data=ujson.dumps(
        data), headers={'Content-Type': 'application/json'})

    # Print the response
    print(response.text)

    # Delay for 10 minutes (600 seconds) before taking the next reading
    time.sleep(600)
