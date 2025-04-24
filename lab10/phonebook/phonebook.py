from config import load_config
from databaseconnect import connect
import csv

def add_user():
    name = input("Введите имя пользователя: ")
    phone = input("Введите номер телефона: ")
    try: 
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO phonebook (phone_user, phone_number) VALUES (%s, %s)", (name, phone)
                )
    except Exception as e:
        print("Error:", e)
    
def find_user():
    key = input("Введите имя или номер для поиска: ")
    try:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE phone_user ILIKE %s OR phone_number LIKE %s",
                (f"%{key}%", f"%{key}%")
            )
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("Ничего не найдено.")
    except Exception as e:
        print("Ошибка при поиске:", e)

def update_user():
    key = input("Введите чо надо обновить: ")
    new_name = input("Новое имя (не пишите ничего если обновлять не нужно): ")
    new_number = input("Новый номер телефона (не пишите ничего если обновлять не нужно: ")
    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                if new_name:
                    cur.execute(
                        "UPDATE phonebook SET phone_user = %s WHERE phone_user = %s OR phone_number = %s",
                        (new_name, key, key)
                    )
                if new_number:
                    cur.execute(
                        "UPDATE phonebook SET phone_number = %s WHERE phone_user = %s or phone_number = %s",
                        (new_number, key, key)
                    )
    except Exception as e:
        print("Ошибка при обновлении:", e)

def delete_user():
    key = input("Введите имя или номер пользователя для удаления: ")
    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM phonebook WHERE phone_user = %s OR phone_number = %s",
                    (key, key)
                )
        print("Пользователь удалён.")
    except Exception as e:
        print("Ошибка при удалении:", e)

def upload_from_csv():
    path = input("Введите путь до CSV-файла: ")
    try:
        conn = connect()
        with conn:
            with conn.cursor() as cur:
                with open(path, newline = '', encoding = 'UTF-8') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if len(row) == 2:
                            cur.execute(
                                "INSERT INTO phonebook (phone_user, phone_number) VALUES (%s, %s)",
                                (row[0], row[1]) 
                            )
        print("Данные успешно загружены")
    except Exception as e:
        print("Ошибка при загрузке файла:", e)

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить пользователя")
        print("2. Найти пользователя")
        print("3. Обновить данные")
        print("4. Удалить пользователя")
        print("5. Добавление пользователей через CSV")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            find_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            upload_from_csv()
        elif choice == '0':
            print("Выход...")
            break
        else:
            print("Неверный выбор!")

if __name__ == '__main__':
    main()
