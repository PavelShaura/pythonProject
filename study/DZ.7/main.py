import utils

questions = utils.load_quest_from_json()

points, correct, incorrect = 0, 0, 0

question_asked = 0
question_total = utils.scum_me_question_total(questions)

while question_asked < question_total:

    utils.show_field(questions)
    user_input = input().title()
    user_data = utils.parse_input(user_input)

    if not user_data:
        print("Такого вопроса нет, попробуйте еще раз!")
        continue

    category, price = user_data["category"], user_data["price"]

    question = questions[category][price]

    if question["asked"]:
        print("Этот вопрос уже был")
        continue

    utils.show_question(question["question"])

    user_answer = input().lower()

    if user_answer == question["answer"]:
        points += int(price)
        correct += 1
        print(f"Верно +{price}. Ваш счет = {points}")

    else:
        points -= int(price)
        incorrect -= 1
        print(f"Неверно, на самом деле - {question['answer']}. Минус {price} баллов. Ваш счет = {points}")

    question["asked"] = True
    question_asked += 1

utils.show_stats(points, correct, incorrect)
utils.save_results(points, correct, incorrect)
