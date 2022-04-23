count_in = 0
sum_in = 0
bad_strip = 0

with open("write.txt") as file:
    for line in file:
        bad_strip += 1
        if line.count(" ") < 1:
            print(f"В строке {bad_strip} ошибка ")
            continue
        data, numb = line.strip().split(" ")
        count_in += 1
        sum_in += int(numb)
print(count_in)
print(sum_in)
