MIN_LENGTH = 6


def main():
    password = get_password(MIN_LENGTH)
    print('*' * len(password))


def get_password(min_length):
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter password: ")
    return password


main()