import unittest

from src.board.board import Board
from src.board.fieldstate import FieldState


class TestBoardGroup(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(size=13)
        self.board[(0, 0)] = FieldState.BLACK
        self.board[(0, 5)] = FieldState.WHITE
        self.board[(3, 3)] = FieldState.BLACK
        self.board[(4, 4)] = FieldState.BLACK

    def test_empty_group(self):
        with self.assertRaises(ValueError):
            self.board.group((11, 9))

    def test_single_stone_on_the_edge(self):
        self.assertEqual(self.board.group((0, 0)), [(0, 0), ])

    def test_single_stone_in_the_corner(self):
        self.assertEqual(self.board.group((0, 5)), [(0, 5), ])

    def test_single_stone_with_diagonal(self):
        self.assertEqual(self.board.group((3, 3)), [(3, 3), ])
        self.assertEqual(self.board.group((4, 4)), [(4, 4), ])
