class Bowling(object):
    def __init__(self):
        self.rolls = list()
    
    def roll(self, pins):
        self.rolls.append(pins)

    def calculate_score(self):
        counter = 0
        score = 0
        
        for i in range(10):
            first_roll = self.rolls[counter]
            second_roll = self.rolls[counter+1]
            
            if self.__is_strike(first_roll):
                third_roll = self.rolls[counter+2]
                score += first_roll + second_roll + third_roll
                counter += 1
            elif self.__is_spare(first_roll, second_roll):
                third_roll = self.rolls[counter+2]
                score += first_roll + second_roll + third_roll
                counter += 2
            else:
                score += first_roll + second_roll
                counter += 2

        return score
    
    def __is_strike(self, first):
        if first == 10:
            return 1
        return 0
    
    def __is_spare(self, first, second):
        if self.__is_strike(first) or first + second != 10:
            return 0
        return 1