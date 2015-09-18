#!/usr/bin/python

import unittest
from bowling.game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_guttergame(self):
        g = self.game
        self.roll_many(0, 20)
        self.assertEquals(0, g.calculate_score(), 'got gutter game score 0')

    def test_one_pin_game(self):
        g = self.game
        g.roll(1)
        self.roll_many(0, 19)
        self.assertEquals(1, g.calculate_score(), 'got one pin game score 1')

    def roll_many(self, pins, rolls):
        g = self.game
        for i in range(rolls):
            g.roll(pins)

if __name__ == '__main__':
    unittest.main()
