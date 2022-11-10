from turtle import *
from bezier import CubicBezier

from paintassistant import PaintAssistant


# We need to scale the original coordinates to fit the screen
c = lambda x: x / 3

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


if __name__ == '__main__':
    s = Screen()
    assistant = PaintAssistant()
    setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    setworldcoordinates(0, SCREEN_HEIGHT, SCREEN_WIDTH, 0)

    with assistant.fill("#9a9794"):
        moveto(522.00,638.67)
        bezier_cubic(522.00,638.67, 522.00,638.67, 652.00,904.67, 522.00,938.67)
        bezier_cubic(522.00,938.67, 390.67,938.00, 522.67,638.00, 522.67,638.00)

    s.mainloop()

