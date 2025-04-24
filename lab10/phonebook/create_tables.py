import psycopg2
from config import load_config

def create_table():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            phone_user VARCHAR(100) NOT NULL,
            phone_number VARCHAR(20) UNIQUE NOT NULL
        )
        """,
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
        print("Phonebook implemented")
    except (psycopg2.DatabaseError, Exception) as error:
        print (error)

if __name__ == '__main__':
    create_table()