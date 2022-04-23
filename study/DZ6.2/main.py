import random


def get_words():
    path = "words.txt"

    with open(path, "r") as fp:
        lines = fp.read()
        words = lines.splitlines()

    return words


def shuffle_word(word):
    word_as_list = list(word)
    random.shuffle(word_as_list)
    return "".join(word_as_list)


def save_score(user_name, user_score):
    path = "history.txt"
    with open(path, 'a') as fp:
        fp.write(f"{user_name} {user_score}\n")


def get_statistics():
    path_1 = "history.txt"
    scores = []

    with open(path_1, "r") as fp:
        for line in fp:
            score = line.strip().split(" ")[-1]
            scores.append(int(score))

    max_score = max(scores)
    len_score = len(scores)

    return {"max": max_score, "len": len_score}


def main():
    user_score = 0

    print("Введите ваше имя")
    user_name = input()

    words = get_words()

    for word in words:
        word_shuffled = shuffle_word(word)
        print(f"Угадайте слово {word_shuffled}")

        user_input = input()

        if user_input == word:
            user_score += 10
            print("Верно! Вы получаете 10 очков.")
        else:
            print(f"Неверно! Верный ответ - {word}")

    save_score(user_name, user_score)
    stats = get_statistics()

    print(f"Всего игр сыграно: {stats.get('len')}")
    print(f"Максимальный рекорд: {stats.get('max')}")


main()
