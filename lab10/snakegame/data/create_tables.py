import psycopg2
from config import load_config

def create_table():
    commands = (
    """
    CREATE TABLE game_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
    );
    """,
    """CREATE TABLE user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES game_user(id) ON DELETE CASCADE,
    score INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    state JSONB
    );
    """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
        print("Tables created")
    except (psycopg2.DatabaseError, Exception) as error:
        print (error)

if __name__ == '__main__':
    create_table()