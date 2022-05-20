from typing import Dict, Tuple, List, Callable, Any

from src.board.fieldstate import FieldState


class Board:

    def __init__(self, size: int):
        self.__size = size
        self.__board: Dict[Tuple[int, int], FieldState] = {
            (x, y): FieldState.EMPTY for x in range(self.__size) for y in range(self.__size)
        }

    @property
    def size(self) -> int:
        return self.__size

    def __getitem__(self, pos: Tuple[int, int]) -> FieldState:
        self.__validate_index(pos)
        return self.__board[pos]

    def __setitem__(self, pos: Tuple[int, int], value: FieldState):
        self.__validate_index(pos)
        self.__board[pos] = value

    def bind(
            self,
            pos: Tuple[int, int],
            p: Callable[[Tuple[int, int]], bool],
            f: Callable[[Any, Tuple[int, int]], Any],
            e: Any
    ):
        """
        Like a Haskell bind, but on the dfs procedure.
        :param pos: position on the board
        :param p: predicate to determine if given position will be processed by dfs
        :param f: evaluation of given position
        :param e: neutral element of f
        :return: result of the evaluation (f)
        """
        visited = {(i, j): False for i in range(self.__size) for j in range(self.__size)}
        v, result, to_visit = None, e, [pos, ]
        while len(to_visit) > 0:
            v = to_visit.pop()
            if p(v):
                visited[v] = True
                result = f(result, v)
                to_visit.extend([x for x in self.neighbours(v) if not visited[x] and p(x)])
        return result

    def group(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Identification of group of a stone at a given position.
        :param pos: position of a given stone
        :return: list of all positions of stones belonging to the same group as a stone on a given position
        """
        self.__validate_non_empty_state(pos)
        return self.bind(
            pos,
            p=lambda v: self.__board[v] == self.__board[pos],
            f=lambda x, y: x + [y],
            e=list()
        )

    def liberties(self, pos: Tuple[int, int]) -> int:
        self.__validate_non_empty_state(pos)
        return self.bind(
            pos,
            p=lambda v: self.__board[v] == self.__board[pos],
            f=lambda x, v: x + len([x for x in self.neighbours(v) if self.__board[x] == FieldState.EMPTY]),
            e=0
        )

    def neighbours(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:

        up, down = (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)
        left, right = (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1])

        return [x for x in [up, down, left, right] if 0 <= x[0] < self.__size and 0 <= x[1] < self.__size]

    def __validate_index(self, pos):
        x, y = pos
        if not 0 <= x <= self.__size - 1 or not 0 <= y <= self.__size - 1:
            raise IndexError(
                f"{str(__class__)}.__getitem__ given value of x, y {pos}, but the boar d size is {self.__size}")

    def __validate_non_empty_state(self, pos):
        if self.__board[pos] == FieldState.EMPTY:
            raise ValueError(f"{__class__}.group, state at given pos {pos} is {self.__board[pos]}")
