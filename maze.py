from cell import *
import time

class Maze:
    def __init__(self,x,y,num_rows,num_cols,cell_size_x,cell_size_y,win):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for j in range(0,self.num_cols)] for i in range(0,self.num_rows)]
        for i in range(0,self.num_rows):
            for j in range(0,self.num_cols):
                self._draw_cell(i,j)
        self._animate()
    
    def _draw_cell(self,i,j):
        x = self.x + self.cell_size_x * i
        y = self.y + self.cell_size_y * j
        self._cells[i][j].draw(x,y,x+self.cell_size_x,y+self.cell_size_y)
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

