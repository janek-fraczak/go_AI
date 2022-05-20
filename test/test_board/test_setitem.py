import unittest

from src.board.board import Board
from src.board.fieldstate import FieldState


class TestBoardGetitem(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(size=13)

    def test_exception_second_coordinate(self):
        with self.assertRaises(IndexError):
            state = self.board[(3, -2)]

    def test_exception_first_coordinate(self):
        with self.assertRaises(IndexError):
            state = self.board[(100, 5)]

    def test_change_state(self):
        self.board[(0, 0)] = FieldState.BLACK
        self.assertEqual(self.board[(0, 0)], FieldState.BLACK)


