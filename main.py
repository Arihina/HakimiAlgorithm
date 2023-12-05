import gui
from Hakimi_algorithm import solve

if __name__ == "__main__":
    gui.run()
    if gui.MATRIX is not None:
        solve(gui.MATRIX)
    else:
        raise Exception("Sorry. Everything fell down")
