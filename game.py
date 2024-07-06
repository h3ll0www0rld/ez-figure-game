from enum import Enum


class block(Enum):
    WHITE = 1
    YELLOW = 2
    PURPLE = 3
    CYAN = 4
    EMPTY = 5


class FigureGame:
    def __init__(self, figures: list[list[block]], step: int) -> None:
        self.STEP = step
        self.CURRENT_STEP = 0
        self.FIGURES = figures
        self.TO_CLEAR = []

    def eliminate(self, position: tuple[int]) -> None:
        self.TO_CLEAR = [position]
        self._eliminate()
        for item in self.TO_CLEAR:
            self.FIGURES[item[0]][item[1]] = block.EMPTY
        for i in range(1, 5):
            for j in range(5):
                self._drop([i, j])
        self.CURRENT_STEP += 1

    def isWin(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.FIGURES[i][j] != block.EMPTY:
                    return False
        return True

    def isLose(self) -> bool:
        if self.CURRENT_STEP == self.STEP:
            return True
        return False

    def getElimatedBlockNum(self) -> int:
        return len(self.TO_CLEAR)

    def _eliminate(self) -> None:
        for i in range(5):
            for j in range(5):
                if (i, j) not in self.TO_CLEAR:
                    for item in self.TO_CLEAR:
                        if (
                            self.FIGURES[i][j]
                            == self.FIGURES[item[0]][item[1]]
                            and self._getDistance((i, j), item) == 1
                        ):
                            self.TO_CLEAR.append((i, j))
                            self._eliminate()

    def _drop(self, position: tuple[int]) -> None:
        p, q = position
        if self.FIGURES[p - 1][q] == block.EMPTY and p > 0:
            self.FIGURES[p - 1][q] = self.FIGURES[p][q]
            self.FIGURES[p][q] = block.EMPTY
            self._drop((p - 1, q))

    def _getDistance(self, position1: tuple[int], position2: tuple[int]):
        return (
            (position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2
        ) ** 0.5
