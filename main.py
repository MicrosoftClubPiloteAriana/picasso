from turtle import *
from bezier import CubicBezier

from paintassistant import PaintAssistant


c = lambda x: x / 3

SCREEN_WIDTH = c(1200)
SCREEN_HEIGHT = c(1434)


def moveto(x, y):
    penup()
    goto(c(522.00), c(638.67))
    pendown()


def bezier_cubic(startx, starty, x1, y1, x2, y2, endx, endy):
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

