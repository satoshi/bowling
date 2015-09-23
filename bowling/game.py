from bowling.frame import BowlingFrame


class BowlingGame(object):

    def __init__(self):
        self.rolls = list()

    def roll(self, pins):
        self.rolls.append(pins)

    def calculate_score(self):
        score = 0
        index = 0

        for i in range(10):
            first_roll = self.rolls[index]
            second_roll = self.rolls[index + 1]

            try:
                third_roll = self.rolls[index + 2]
                f = BowlingFrame([first_roll, second_roll, third_roll])
            except IndexError:
                f = BowlingFrame([first_roll, second_roll])

            score += f.calculate_score()
            index += f.calculate_offset()

        return score
