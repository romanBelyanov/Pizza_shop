def hi():
    print("Здравствуйте! Выберите действие:")
    print("1 - Регистрация")
    print("2 - Авторизация")
    ans = int(input())
    if ans >= 2:
        return 2
    else:
        return 1