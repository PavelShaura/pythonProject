from question import Question
from utils import load_questions
from utils import count_correct_answers
from utils import count_point


def main():
    questions = load_questions()

    for question in questions:

        print(question.build_question())
        user_answer = input()
        question.user_answer = user_answer

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    correct_counter = count_correct_answers(questions)
    points = count_point(questions)

    print("Вот и все!")
    print(f"Отвечено {correct_counter} вопрпоса из {len(questions)}")
    print(f"Набрано баллов {points}")


main()
