import unittest

from src.board.board import Board


class TestBoardGetitem(unittest.TestCase):

    def setUp(self) -> None:
        self.board_to_test = Board(size=9)

    def test_exception_second_coordinate(self):
        with self.assertRaises(IndexError):
            state = self.board_to_test[(0, 100)]

    def test_exception_first_coordinate(self):
        with self.assertRaises(IndexError):
            state = self.board_to_test[(100, 0)]

    def test_no_exception_raised(self):
        try:
            state = self.board_to_test[(2, 3)]
        except IndexError:
            self.fail(f"exception raised for board size {self.board_to_test.size}")
