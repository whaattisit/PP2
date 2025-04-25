import psycopg2
from data.config import load_config

def connect():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка подключения к базе данных:", error)

if __name__ == '__main__':
    connect()