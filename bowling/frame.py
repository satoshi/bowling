from numpy import roll


class BowlingFrame(object):

    def __init__(self, rolls):
        self.rolls = rolls

    def calculate_score(self):
        score = 0

        for roll in self.rolls:
            score += roll
        return score

    def calculate_offset(self):
        return 2
