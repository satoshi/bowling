class BowlingGame(object):

    def __init__(self):
        self.score = 0

    def roll(self, pins):
        self.score += pins

    def calculate_score(self):
        return self.score
