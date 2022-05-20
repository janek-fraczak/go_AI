from typing import Tuple

from src.board.board import Board
from src.board.fieldstate import FieldState


class StateManager:
    def __init__(self, prev_board: Board, now_board: Board):
        pass

    def validate_move(self, pos: Tuple[int, int], field_state: FieldState) -> None:
        pass
