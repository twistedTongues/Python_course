creds = {'name1': 'pass1', 'name2': 'pass2', 'name3': 'pass3'}


def new_user():
    users_name = input('Create a login: ')
    creds[users_name] = input('Create a password: ')
    print()


def auth_required(func):
    def wrapper_decorator(*args):
        login = input('Enter ur login: ')
        password = input('Enter ur password: ')
        if login in creds and creds[login] == password:
            return func(*args)
        else:
            print('\n\t\t\tUr login or password is wrong')
            choice = input("If u want to create new account type 'y' or 'n' \
to try again: ")
            if choice == 'y':
                new_user()
                return wrapper_decorator(*args)
            elif choice == 'n':
                return wrapper_decorator(*args)
    return wrapper_decorator


@auth_required
def some_func():
    print("\n\nThis function multiply two numbers!")
    f_n = int(input('Enter ur first number: '))
    s_n = int(input('Enter ur second number: '))
    return(f"Ur result = {f_n * s_n}")


res = some_func()
print(res)
