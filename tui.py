from game import FigureGame, block
from figures import figures


def printBoard(figures: list[list[block]]):
    for line_num in range(4, -1, -1):
        line = figures[line_num]
        print(
            "{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                line[0], line[1], line[2], line[3], line[4]
            )
        )


if __name__ == "__main__":
    fg = FigureGame(
        figures,
        9,
    )
    printBoard(fg.FIGURES)
    while 1:
        if fg.isWin():
            print("You Win.")
            exit()
        if fg.isLose():
            print("You Lose. Try Again.")
            exit()
        fg.eliminate((0, int(input("which block? (0 ~ 4) > "))))
        printBoard(fg.FIGURES)
