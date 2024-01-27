from graphics import Line, Point

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._ulx = None
        self._uly = None
        self._lrx = None
        self._lry = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._ulx = x1
        self._uly = y1
        self._lrx = x2
        self._lry = y2
        if self._win is None:
            return
        color = "white"
        if self.has_top_wall:
            color = "black"
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line,color)
        color = "white"
        if self.has_right_wall:
            color = "black"
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line,color)
        color = "white"
        if self.has_bottom_wall:
            color = "black"
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line,color)
        color = "white"
        if self.has_left_wall:
            color = "black"
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line,color)
    
    def draw_move(self, to_cell,undo=False):
        ax = (self._ulx + self._lrx) / 2
        ay = (self._uly + self._lry) / 2
        bx = (to_cell._ulx + to_cell._lrx) / 2
        by = (to_cell._uly + to_cell._lry) / 2
        color = "red"
        if undo:
            color = "gray"
        line = Line(Point(ax,ay),Point(bx,by))
        self._win.draw_line(line,color)