from cell import *
import time
import random

class Maze:
    def __init__(self,x,y,num_rows,num_cols,cell_size_x,cell_size_y,win = None,seed = None):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if not seed is None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))

            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(to_visit))
            next = to_visit[direction]

            if next[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if next[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if next[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if next[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for item in col:
                item.visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        current = self._cells[i][j]
        self._animate()
        current.visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        #-------------------------
        if i > 0 and not self._cells[i - 1][j].visited:
            if not self._cells[i-1][j].has_right_wall and not current.has_left_wall:
                current.draw_move(self._cells[i-1][j])
                value = self._solve_r(i-1,j)
                if value:
                    return value
                else:
                    current.draw_move(self._cells[i-1][j],True)

        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
            if not self._cells[i+1][j].has_left_wall and not current.has_right_wall:
                current.draw_move(self._cells[i+1][j])
                value = self._solve_r(i+1,j)
                if value:
                    return value
                else:
                    current.draw_move(self._cells[i+1][j],True)

        if j > 0 and not self._cells[i][j - 1].visited:
            if not self._cells[i][j-1].has_bottom_wall and not current.has_top_wall:
                current.draw_move(self._cells[i][j-1])
                value = self._solve_r(i,j-1)
                if value:
                    return value
                else:
                    current.draw_move(self._cells[i][j-1],True)

        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
            if not self._cells[i][j+1].has_top_wall and not current.has_bottom_wall:
                current.draw_move(self._cells[i][j+1])
                value = self._solve_r(i,j+1)
                if value:
                    return value
                else:
                    current.draw_move(self._cells[i][j+1],True)
        return False

            