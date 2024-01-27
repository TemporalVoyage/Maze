from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(0,0,6,8,100,100,win)
    maze.solve()
    win.wait_for_close()

main()