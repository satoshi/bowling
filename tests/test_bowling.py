#!/usr/bin/python

import unittest
from bowling.game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_guttergame(self):
        g = self.game
        self.roll_many(0, 20)
        self.assertEquals(0, g.calculate_score(), 'gutter game score 0')

    def test_one_pin_game(self):
        g = self.game
        g.roll(1)
        self.roll_many(0, 19)
        self.assertEquals(1, g.calculate_score(), 'one pin game score 1')

    def test_one_spare(self):
        g = self.game
        g.roll(7)
        g.roll(3)
        g.roll(5)
        self.roll_many(0, 17)
        self.assertEquals(20, g.calculate_score(), 'one spare game score 20')

    def test_one_strike(self):
        g = self.game
        g.roll(10)
        g.roll(2)
        g.roll(4)
        self.roll_many(0, 17)
        self.assertEquals(22, g.calculate_score(), 'one strike game score 22')

    def test_perfect_game(self):
        g = self.game
        self.roll_many(10, 12)
        self.assertEquals(300, g.calculate_score(), 'perfect game score 300')

    def roll_many(self, pins, rolls):
        g = self.game
        for i in range(rolls):
            g.roll(pins)

if __name__ == '__main__':
    unittest.main()
