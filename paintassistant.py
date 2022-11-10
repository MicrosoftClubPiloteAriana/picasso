import turtle


class PaintAssistant:
    @staticmethod
    def fill(color):
        return FillHelper(color)


class FillHelper:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        return self

    def __exit__(self, type, value, traceback):
        turtle.end_fill()
