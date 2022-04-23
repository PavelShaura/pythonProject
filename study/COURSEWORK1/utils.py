import json
from random import shuffle
import requests
from basicword import Basicwords


def load_word():
    list_in = requests.get("https://jsonkeeper.com/b/51PK")
    data = json.loads(list_in.text)
    return data


def get_questions(data):
    questions = []

    for question_data in data:
        question = Basicwords(question_data['word'], question_data['subwords'])
        questions.append(question)

    return questions


def get_random_question(questions):
    if len(questions) > 0:
        shuffle(questions)
        return questions[0]
    return None
