virus_code = 'print("I am VIRUS")'

with open("write.py", "a") as file:  # append
    file.write(f"\n{virus_code}\n")
