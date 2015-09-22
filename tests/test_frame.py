#!/usr/bin/python

import unittest
from bowling.frame import BowlingFrame


class TestBowlingFrame(unittest.TestCase):

    def test_normal_frame(self):
        f = BowlingFrame([3, 5])
        self.assertEquals(f.calculate_score(), 8, 'got 8 for the frame')
        self.assertEquals(f.calculate_offset(), 2, 'got 2 for offset')

#     def test_spare_frame(self):
#         f = BowlingFrame([6, 4, 8])
#         self.assertEquals(f.calculate_score(), 18, 'got 18 for the frame')

if __name__ == '__main__':
    unittest.main()
