virus_code = "I am VIRUS"

with open("write.py") as file:
    content = file.read()
    if virus_code in content:
        print("Вирус обнаружен")
    else:
        print("Вирусов нет")
