from player import Player
from utils import *

print("Введите имя игрока")

name = input()
player = Player(name)

data = load_word()

questions = get_questions(data)

question = get_random_question(questions)

count_words = question.count_sub_words()

print(f"Привет, {name}\nСоставьте {count_words} слов из слова {question.word}\n"
      f"Слова должны быть не короче 3 букв\n"
      f"Чтобы закончить игру, угадайте все слова или напишите 'стоп'\n"
      f"Поехали, ваше первое слово?")

while True:

    answer = input()

    if answer == "стоп" or len(question.subwords) == len(player.answers):
        break

    if not question.is_correct(answer):
        print("Неверно")

    elif player.is_answer(answer):
        print("Уже было")

    else:
        player.set_answer(answer)
        print("Верно")

print("Cлова закончились, игра завершена!")
print(f"Вы угадали {player.score()} слов")
