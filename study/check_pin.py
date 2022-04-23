def check_pin(pin):
    for i in pin:
        if pin != "1234" and len(pin) == 4 and pin.isdigit() and pin.count(i) < 3:
            return True
        else:
            return False


print(check_pin("2222"))
