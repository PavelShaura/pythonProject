user_lang = input("Какой язык вы учите: ")
user_time = input("Как долго: ")
user_place = input("Где именно: ")

with open("write.txt", "wt") as file:
    file.write(f"{user_lang}\n")
    file.write(f"{user_time}\n")
    file.write(f"{user_place}\n")

print("Ответы записаны в файл write.txt")
