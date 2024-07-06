from game import FigureGame, block
from figures import figures


for a in range(5):
    for b in range(5):
        for c in range(5):
            for d in range(5):
                for e in range(5):
                    for f in range(5):
                        for g in range(5):
                            for h in range(5):
                                for i in range(5):
                                    fg = FigureGame(
                                        figures,
                                        9,
                                    )
                                    fg.eliminate((0, a))
                                    if fg.FIGURES[0][b] == block.EMPTY:
                                        break
                                    fg.eliminate((0, b))
                                    if fg.FIGURES[0][c] == block.EMPTY:
                                        break
                                    fg.eliminate((0, c))
                                    if fg.FIGURES[0][d] == block.EMPTY:
                                        break
                                    fg.eliminate((0, d))
                                    if fg.FIGURES[0][e] == block.EMPTY:
                                        break
                                    fg.eliminate((0, e))
                                    if fg.FIGURES[0][f] == block.EMPTY:
                                        break
                                    fg.eliminate((0, f))
                                    if fg.FIGURES[0][g] == block.EMPTY:
                                        break
                                    fg.eliminate((0, g))
                                    if fg.FIGURES[0][h] == block.EMPTY:
                                        break
                                    fg.eliminate((0, h))
                                    if fg.FIGURES[0][i] == block.EMPTY:
                                        break
                                    fg.eliminate((0, i))
                                    if fg.isWin():
                                        print(a, b, c, d, e, f, g, h, i)
                                        exit()
