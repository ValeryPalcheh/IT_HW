def request_admin_login(func):
    def wrapper():
        login = input("Введите логин админа: ")
        if login == "admin":
            func()
        else:
            print("Доступ запрещен!")
        
    return wrapper

@request_admin_login
def show_balance():
    balance = 5000
    print(f'Сумма на счете: {balance} рублей')

show_balance()