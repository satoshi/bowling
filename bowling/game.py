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

            if first_roll == 10:
                third_roll = self.rolls[index + 2]
                score += first_roll + second_roll + third_roll
                index += 1
            elif first_roll + second_roll == 10:
                third_roll = self.rolls[index + 2]
                score += first_roll + second_roll + third_roll
                index += 2
            else:
                score += first_roll + second_roll
                index += 2

        return score
