import json
from model import age_Check
def hi():
    print("Здравствуйте! Выберите действие:")
    print("1 - Регистрация")
    print("2 - Авторизация")
    ans = int(input())
    if ans >= 2:
        return 2
    else:
        return 1

def show_menu(path):
    dct = {"pizzas": "Пиццы:", "drinks": "Напитки: ", "alcohol": "Алкоголь: "}
    with open(path, "r") as file:
        res = json.load(file)
    for food in res['menu']:
        if food == 'alcohol' and not age_Check():
            continue
        print(dct[food])
        for param in res['menu'][food]:
            print(f"Название: {param['name']} Цена: {param['price']}")

show_menu(r"C:\Users\Белянов Роман ИИ-71\PycharmProjects\pizza\menu.json")
