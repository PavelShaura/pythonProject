filename = "user_data.txt"
f = open(filename, "r")
name = f.readline()
surname = f.readline()
email = f.readline()
phone = f.readline()

print(f"{name} {surname} – это вы. Ваша почта {email}, ваш телефон {phone}")
