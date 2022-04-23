class Question:

    def __init__(self, question_text, question_diff, question_answer):
        self.question_text = question_text
        self.question_diff = question_diff
        self.question_answer = question_answer

        self.is_asked = False
        self.user_answer = None
        self.points = self.question_diff * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.user_answer == self.question_answer

    def build_question(self):
        answer = f"Вопрос: {self.question_text}\nСложность: {self.question_diff}/5"
        return answer

    def build_positive_feedback(self):
        answer = f"Ответ верный, получено {self.points} баллов"
        return answer

    def build_negative_feedback(self):
        answer = f"Ответ неверный. Верный ответ - {self.question_answer}"
        return answer

    def __repr__(self):
        return f"{self.question_text} - {self.question_answer} ({self.question_diff}/5)"
