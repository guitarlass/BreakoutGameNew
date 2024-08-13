import random
import turtle
from ball import Ball
from paddle import Paddle
from brick import Brick
import random

screen = turtle.Screen()
screen.title("Breakout Game")
screen.setup(height=500, width=800)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
paddle = Paddle()

bricks = []
brick_colors = ['green', 'yellow', 'orange', 'red']
brick_lengths = [4, 3, 2]

end_x, end_y = (400, 160)
current_x, current_y = (-400, 0)
space = 10
brick_space_half = 5
space_btw_lines_half = brick_space_half
brick_width = 2
full_half_width = brick_width * 20 / 2
line_index = 0

while current_x <= end_x and current_y <= end_y:
    # if current_x >= 320:
    #     brick_len = ((400 - current_x) / 2 - space) / 20
    # else:
    print(current_x)
    brick_len = random.choice(brick_lengths)
    current_x = current_x + brick_len * 20 / 2
    brick = Brick(current_x, current_y, brick_len, brick_width, brick_colors[line_index])
    current_x = current_x + brick_len * 20 / 2 + space
    if current_x + brick_len * 20 / 2 + space >= 400:
        print(current_x)
        current_y = current_y + brick_width * 20 + space
        current_x = -400
        line_index += 1
        print("---------------")
    bricks.append(brick)

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

while True:
    screen.update()
    ball.move()

    if ball.xcor() >= 380 or ball.xcor() <= -385:
        ball.bounce_x()
    elif ball.ycor() >= 235:
        ball.bounce_y()

    if ball.ycor() <= -215:  # ball.distance(paddle) <= 50 and
        ball.bounce_y()

    for brick_obj in bricks:
        size = brick_obj.shapesize()
        length = size[1]
        half_height = length * 20 / 2
        if (
                brick_obj.xcor() - full_half_width - brick_space_half < ball.xcor() < brick_obj.xcor() + full_half_width + brick_space_half and
                brick_obj.ycor() - half_height - space_btw_lines_half < ball.ycor() < brick_obj.ycor() + half_height + space_btw_lines_half):
            # Determine which direction the collision occurred from
            if abs(ball.xcor() - brick_obj.xcor()) > abs(ball.ycor() - brick_obj.ycor()):
                ball.bounce_x()
            else:
                ball.bounce_y()
            brick_obj.hideturtle()
            bricks.remove(brick_obj)
