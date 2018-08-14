"""Samuel Hayes"""


def main():
    min_length = 6
    password = get_password(min_length)

    password_hider(password)


def password_hider(password):
    print("*" * len(password))


def get_password(min_length):
    password = str(input("Password: "))
    while len(password) < min_length:
        print("Password length too short")
        password = str(input("Password: "))
    return password


main()
