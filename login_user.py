'''
Login function
'''
from data import personnel


logged_in = False


def is_logged_in():
    return logged_in


def login():
    global logged_in
    username = input("Username: ")
    password = input("Password: ")
    for person in personnel:
        if username == person.get("user_name"):
            if password == person.get("password"):
                print(f"Welcome back {username}")
                logged_in = True
                return True
            else:
                print("Wrong password")
                logged_in = False
                return False


if __name__ == '__main__':
    login()
    is_logged_in()
