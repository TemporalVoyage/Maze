import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_width(self):
        num_cols = 12
        num_rows = 10
        widthx = 50
        widthy = 10
        m1 = Maze(0, 0, num_rows, num_cols, widthx, widthy)
        self.assertEqual(
            len(m1._cells)*m1.cell_size_x,
            num_cols*widthx,
        )
        self.assertEqual(
            len(m1._cells[0])*m1.cell_size_y,
            num_rows*widthy,
        )
    
    def test_maze_start_end(self):
        num_cols = 12
        num_rows = 10
        widthx = 50
        widthy = 10
        m1 = Maze(0, 0, num_rows, num_cols, widthx, widthy)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False,
        )

    def test_reset(self):
        num_cols = 12
        num_rows = 10
        widthx = 50
        widthy = 10
        m1 = Maze(0, 0, num_rows, num_cols, widthx, widthy)
        for list in m1._cells:
            for cell in list:
                self.assertFalse(cell.visited)
                
unittest.main()