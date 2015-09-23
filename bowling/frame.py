class BowlingFrame(object):

    def __init__(self, rolls):
        self.rolls = rolls

    def calculate_score(self):
        first_roll = self.rolls[0]
        second_roll = self.rolls[1]

        if self.__is_strike() or self.__is_spare():
            third_roll = self.rolls[2]
            return first_roll + second_roll + third_roll

        return first_roll + second_roll

    def calculate_offset(self):
        if self.__is_strike():
            return 1
        return 2

    def __is_strike(self):
        first_roll = self.rolls[0]

        if first_roll == 10:
            return 1
        return 0

    def __is_spare(self):
        first_roll = self.rolls[0]
        second_roll = self.rolls[1]

        if first_roll + second_roll == 10:
            return 1
        return 0
