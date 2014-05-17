#!/usr/bin/env python

import sys
import os
import unittest

findbin = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.append(findbin + "/../modules")

from bowling import Bowling

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.game = Bowling()

    def test_gutter_game(self):
        g = self.game
        self.roll_many(20, 0)
        self.assertEqual(0, g.calculate_score(), 'gutter game 0 points')

    def test_one_pin_game(self):
        g = self.game
        g.roll(1)
        self.roll_many(19, 0)
        self.assertEquals(1, g.calculate_score(), 'one pin game 1 points')

    def test_one_spare_game(self):
        g = self.game
        g.roll(5)
        g.roll(5)
        g.roll(7)
        self.roll_many(17, 0)
        self.assertEquals(24, g.calculate_score(), 'one spare game 24 points')

    def test_one_strike_game(self):
        g = self.game
        g.roll(10)
        g.roll(2)
        g.roll(3)
        self.roll_many(17, 0)
        self.assertEquals(20, g.calculate_score(), 'one strike game 20 points')

    def test_perfect_game(self):
        g = self.game
        self.roll_many(12, 10)
        self.assertEquals(300, g.calculate_score(), 'perfect game 300 points')

    def roll_many(self, rolls, pins):
        g = self.game

        for i in range(rolls):
            g.roll(pins)

if __name__ == '__main__':
    unittest.main()