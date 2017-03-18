#!/usr/bin/python

from bowling.game import BowlingGame


def setup():
    return BowlingGame()


def roll_many(g, pins, rolls):
    for i in range(rolls):
        g.roll(pins)


def test_guttergame():
    g = setup()
    roll_many(g, 0, 20)
    assert g.calculate_score() == 0, 'gutter game score 0'


def test_one_pin_game():
    g = setup()
    g.roll(1)
    roll_many(g, 0, 19)
    assert g.calculate_score() == 1, 'one pin game score 1'


def test_one_spare():
    g = setup()
    g.roll(7)
    g.roll(3)
    g.roll(5)
    roll_many(g, 0, 17)
    assert g.calculate_score() == 20, 'one spare game score 20'


def test_one_strike():
    g = setup()
    g.roll(10)
    g.roll(2)
    g.roll(4)
    roll_many(g, 0, 17)
    assert g.calculate_score() == 22, 'one strike game score 22'


def test_perfect_game():
    g = setup()
    roll_many(g, 10, 12)
    assert g.calculate_score() == 300, 'perfect game score 300'
