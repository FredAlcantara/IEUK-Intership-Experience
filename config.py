from dotenv import load_dotenv
import mysql.connector as mysql
import os

load_dotenv()

# Initialising secret keys to connect through the database
HOST = os.getenv('DATABASE_HOST')
DATABASE = os.getenv('DATABASE_NAME')
USER = os.getenv('DATABASE_USER')
PASSWORD = os.getenv('DATABASE_PASSWORD')


def db_connection():
    try:
        db = mysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        return db

    except mysql.Error as e:
        print(f'Error connecting to MySQL database: {e}')
        return None


def getDatabase():
    return DATABASE
