from view import hi
import json


def calculate_discounted_price(price, discount):
    return price - (price * discount / 100)
def age_Check():
    try:
        with open("data_user.json", 'r') as file:
            data = file.read()
            file_obj = json.loads(data)
            if 'age' in file_obj:
                print(file_obj['age'])
            else:
                print("Ключ 'age' не найден в данных.")
    except FileNotFoundError:
        print("Файл 'data_user.json' не найден.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    if file_obj['age'] < 18:
        user_young = False
        return user_young
    else:
        user_young = True
        return user_young
age_Check()

def login():

    name = input("Введите логин: ")
    password = input("Введите пароль: ")
    age = int(input("Введите возраст: "))
    user_data = {
        "login": name,
        "password": password,
        "age": age
    }

    try:
        with open("user_data.json", 'w') as file:
            json.dump(user_data, file, ensure_ascii=False, indent=4)
        print("Данные успешно сохранены в файл user_data.json.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


import json


def load_user_data():
    try:
        with open("user_data.json", 'r') as file:
            user_data = json.load(file)


            login = user_data.get("login")
            password = user_data.get("password")

            print(f"Логин: {login}")
            print(f"Пароль: {password}")
    except FileNotFoundError:
        print("Файл 'user_data.json' не найден.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



load_user_data()

