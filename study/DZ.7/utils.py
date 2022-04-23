import json


def load_quest_from_json():
    file = open("data.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    return data


def show_field(questions):
    for quest_name, quest_price in questions.items():
        print(quest_name.ljust(14), end="")
        for price_in, data_in in quest_price.items():
            asked = data_in["asked"]
            if not asked:
                print(price_in.ljust(6), end=" ")
            else:
                print("   ".ljust(6), end=" ")

        print()


def parse_input(user_input):
    user_data = user_input.split(" ")
    if len(user_data) != 2:
        return False
    if not user_data[0].isalpha():
        return False
    if not user_data[1].isdigit():
        return False
    return {"category": user_data[0], "price": user_data[1]}


def show_question(question_name):
    print(f"Слово {question_name} в переводе означает ...")


def show_stats(points, correct, incorrect):
    print("У нас закончились вопросы")
    print()
    print(f"Вас счет: {points}")
    print(f"Верных ответов: {correct}")
    print(f"Неверных ответов: {incorrect}")


def save_results(points, correct, incorrect):
    file = open("results.json", "r", encoding="utf-8")
    results = json.load(file)
    file.close()

    results.append({"points": points, "correct": correct, "incorrect": incorrect})

    file = open("results.json", "w", encoding="utf-8")
    json.dump(results, file)
    file.close()


save_results(1, 1, 1)


def scum_me_question_total(questions):
    all_questions = 0
    for parts in questions.values():
        all_questions += len(parts)
    return all_questions
