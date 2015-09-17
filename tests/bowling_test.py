#!/usr/bin/python

import unittest
from bowling.game import BowlingGame

class TestBowling(unittest.TestCase):
    def test_guttergame(self):
        g = BowlingGame()

if __name__ == '__main__':
    unittest.main()