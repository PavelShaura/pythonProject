alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "


def check_pin(pin):
    for i in pin:
        if pin != "1234" and len(pin) == 4 and pin.isdigit() and pin.count(i) < 3:
            return True
        else:
            return False


print(check_pin("1122"))


def check_pass(password):
    """Проверяет, чтобы пароль был не меньше 8 символов, содержал буквы и цифры.
    """

    return len(password) > 7 and not password.isalpha() and not password.isdigit()


print(check_pass("123frdsfd"))


def check_mail(e_mail):
    if '@' in e_mail and '.' in e_mail:
        return True
    else:
        return False


print(check_mail("mail.asdas@mail.com"))


def check_name(name):
    """
    Проверяет содержание в имени только русских букв и пробелов.
    """
    for letter in name:
        if letter.lower() not in alphabet:
            return False

    return True


print(check_name("Константин"))
