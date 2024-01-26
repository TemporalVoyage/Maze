from graphics import *

def main():
    win = Window(800,600)
    pointA = Point(90,60)
    pointB = Point(700,500)
    lineA = Line(pointA,pointB)
    win.draw_line(lineA)
    win.wait_for_close()

main()