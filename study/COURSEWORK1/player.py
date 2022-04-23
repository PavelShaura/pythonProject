class Player:

    def __init__(self, name):
        self.name = name
        self.answers = []

    def is_answer(self, answer):
        if answer in self.answers:
            return True
        return False

    def set_answer(self, answer):
        self.answers.append(answer)

    def score(self):
        score = len(self.answers)
        return score
