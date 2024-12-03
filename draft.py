password = input('Введите пароль: ')

score = 0


def is_very_long(password):
    if len(password) > 12:
        return True
    else:
        return False


def has_digit(password):
    return True if any(char.isdigit() for char in password) else False


def has_letters(password):
    return True if any(char.isalpha() for char in password) else False


def has_upper_letters(password):
    return True if any(char.isupper() for char in password) else False


def has_lower_letters(password):
    return True if any(char.islower() for char in password) else False


def has_symbols(password):
    return any(not character.isalnum() for character in password)


def main():
    is_very_long(password)
    has_digit(password)
    has_letters(password)
    has_upper_letters(password)
    has_lower_letters(password)
    has_symbols(password)


secure_steps = [
    is_very_long,
    has_digit,
    has_letters,
    has_upper_letters,
    has_lower_letters,
    has_symbols
    ]

for s in secure_steps:
    if s(password):
        score += 2


print('Рейтинг пароля: ', score)


if __name__ == '__main__':
    main()
