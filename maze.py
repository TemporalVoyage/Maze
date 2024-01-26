from cell import *
import time

class Maze:
    def __init__(self,x,y,num_rows,num_cols,cell_size_x,cell_size_y,win = None):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for j in range(0,self.num_rows)] for i in range(0,self.num_cols)]
        for i in range(0,self.num_cols):
            for j in range(0,self.num_rows):
                self._draw_cell(i,j)
        self._animate()
    
    def _draw_cell(self,i,j):
        x = self.x + self.cell_size_x * i
        y = self.y + self.cell_size_y * j
        self._cells[i][j].draw(x,y,x+self.cell_size_x,y+self.cell_size_y)
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

