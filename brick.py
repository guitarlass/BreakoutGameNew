import turtle

class Brick(turtle.Turtle):
    def __init__(self, x_pos, y_pos, brick_len, brick_width, color):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=brick_width, stretch_len=brick_len)
        self.goto(x_pos, y_pos)