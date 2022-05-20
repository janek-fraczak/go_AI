import unittest

from src.board.board import Board
from src.board.fieldstate import FieldState


class TestBoardLibertiesSingleStone(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(size=9)

        self.board[(0, 0)] = FieldState.BLACK
        self.board[(3, 3)] = FieldState.WHITE
        self.board[(6, 0)] = FieldState.BLACK

    def test_corner_stone_liberties(self):
        self.assertTrue(self.board.liberties((0, 0)) == 2)

    def test_side_stone_liberties(self):
        self.assertTrue(self.board.liberties((6, 0)) == 3)

    def test_center_stone_liberties(self):
        self.assertTrue(self.board.liberties((3, 3)) == 4)


class TestBoardLibertiesGroups(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(size=13)

        self.board[(3, 3)] = FieldState.BLACK
        self.board[(3, 4)] = FieldState.WHITE
        self.board[(4, 3)] = FieldState.BLACK
        self.board[(4, 4)] = FieldState.BLACK
        self.board[(2, 4)] = FieldState.BLACK

    def test_one_stone_surrounded(self):
        self.assertTrue(self.board.liberties((3, 4)) == 1)

    def test_group_liberties(self):
        self.assertTrue(self.board.liberties((4, 4)) == 6)

    def test_one_black_stone_liberties(self):
        self.assertTrue(self.board.liberties((2, 4)) == 3)


class TestLibertiesOfEmptyField(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(size=9)

    def test_exception_raise(self):
        with self.assertRaises(ValueError):
            self.board.liberties((0, 0))
