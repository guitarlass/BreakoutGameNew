import turtle


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.color("white")
        self.penup()
        self.goto(0, -230)
        self.speed(0)

    def move_right(self):
        self.setx(self.xcor() + 20)

    def move_left(self):
        self.setx(self.xcor() - 20)
