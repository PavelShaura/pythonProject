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


def save_score(player_name, player_score):
    path = "history.txt"
    with open(path, 'a') as fp:
        fp.write(f"{player_name} {player_score}\n")


def get_statistics():
    path_1 = "history.txt"
    scores = []

    with open(path_1, "r", encoding="utf-8") as fp:
        for line in fp:
            score = line.strip().split(" ")[-1]
            scores.append(score)

    max_score = max(scores)
    len_score = len(scores)

    return {"max": max_score, "len": len_score}


print(get_statistics())
