from turtle import *
from svg.path import path

from bezier import CubicBezier
from paintassistant import PaintAssistant
from parser import PathParser


# We need to scale the original coordinates to fit the screen
c = lambda x: x / 2.5

SCREEN_WIDTH = c(1200)
SCREEN_HEIGHT = c(1434)


def moveto(x, y):
    """
    Moves to a certain point without drawing a line
    """
    penup()
    goto(c(x), c(y))
    pendown()


def bezier_cubic(startx, starty, x1, y1, x2, y2, endx, endy):
    """
    Draws a Bézier curve on the screen
    :param startx: the x-coordinate of the point at the start
    :param starty: the y-coordinate of the point at the start
    :param x1: the x-coordinate of the control point for the start of the curve
    :param y1: the y-coordinate of the control point for the start of the curve
    :param x2: the x-coordinate of the control point for the end of the curve
    :param y2: the y-coordinate of the control point for the end of the curve
    :param endx: the x-coordinate of the point at the start
    :param endy: the x-coordinate of the point at the start
    """
    curve = CubicBezier(startx, starty, x1, y1, x2, y2, endx, endy).calc_curve()
    for x, y in zip(*curve):
        goto(c(x), c(y))


def render_worldcup():
    s = Screen()
    assistant = PaintAssistant()
    setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    setworldcoordinates(0, SCREEN_HEIGHT, SCREEN_WIDTH, 0)
    title("Fifa World Cup 2022")
    speed(5)
    tracer(5, 0)

    for path_segment in PathParser("samples/worldcupqatar2022.xml").svg_path:
        if isinstance(path_segment, path.CubicBezier):
            startx, starty = path_segment.start.real, path_segment.start.imag
            endx, endy = path_segment.end.real, path_segment.end.imag
            x1, y1 = path_segment.control1.real, path_segment.control1.imag
            x2, y2 = path_segment.control2.real, path_segment.control2.imag
            bezier_cubic(startx, starty, x1, y1, x2, y2, endx, endy)

        elif isinstance(path_segment, path.Move):
            x, y = path_segment.start.real, path_segment.start.imag
            moveto(x, y)
    hideturtle()
    s.mainloop()


if __name__ == '__main__':
    render_worldcup()
