#!/usr/bin/python3

from bowling.frame import BowlingFrame


def test_normal_frame():
    f = BowlingFrame([3, 5])
    assert f.calculate_score() == 8, 'got 8 for the frame'
    assert f.calculate_offset() == 2, 'got 2 for offset'


def test_spare_frame():
    f = BowlingFrame([6, 4, 8])
    assert f.calculate_score() == 18, 'got 18 for the frame'
    assert f.calculate_offset() == 2, 'got 2 for offset'


def test_strike_frame():
    f = BowlingFrame([10, 3, 6])
    assert f.calculate_score() == 19, 'got 19 for the frame'
    assert f.calculate_offset() == 1, 'got 1 for offset'
