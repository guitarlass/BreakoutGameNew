import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed(1)
        self.penup()
        self.goto(0, -210)
        self.x_distance = 1.5
        self.y_distance = 1.5

    def move(self):
        self.setx(self.xcor() + self.x_distance)
        self.sety(self.ycor() + self.y_distance)

    def bounce_x(self):
        self.x_distance *= -1

    def bounce_y(self):
        self.y_distance *= -1
