class Basicwords:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def is_correct(self, answer):
        if answer in self.subwords:
            return True
        return False

    def count_sub_words(self):
        return len(self.subwords)
