import random
import turtle
from ball import Ball
from paddle import Paddle
from brick import Brick
import random
import math

score = 0

screen = turtle.Screen()
screen.title("Breakout Game")
screen.setup(height=500, width=800)
screen.bgcolor("black")
screen.tracer(0)

label_score = turtle.Turtle()
label_score.hideturtle()
label_score.color("white")
label_score.penup()
label_score.goto(-380, 210)
label_score.write(score, align="center", font=("Arial", 18, "normal"))

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

# while current_y <= end_y:
#     remaining = end_x - current_x   # Calculate remaining space on the line
#
#     # Check if the remaining space is less than or equal to the width needed for the smallest brick
#     if remaining <= min(brick_lengths) * 20:
#         brick_len = max(1, math.ceil(remaining / 20))  # Ensure at least 1 grid unit width
#     else:
#         brick_len = random.choice(brick_lengths)
#
#     brick_centre_x = current_x + ((brick_len * 20) / 2)
#     brick = Brick(brick_centre_x, current_y, brick_len, brick_width, brick_colors[line_index])
#
#     # Update current_x for the next brick
#     current_x = brick_centre_x + ((brick_len * 20) / 2) + space
#
#     # Append the brick to the list
#     bricks.append(brick)
#
#     # Check if we need to move to the next line
#     if current_x + min(brick_lengths) * 20 / 2 >= end_x:
#         current_y = current_y + brick_width * 20 + space
#         current_x = -400
#         line_index = (line_index + 1) % len(brick_colors)  # Cycle through brick colors
#
# # Print the number of bricks to verify
# print(len(bricks))

while current_x <= end_x and current_y <= end_y:
    remaining = 400-current_x
    if remaining <= 90:
        print(current_x)
        print(remaining)
        brick_len = current_x + math.ceil(remaining // 20)
    else:
        brick_len = random.choice(brick_lengths)
    brick_centre_x = current_x + ((brick_len * 20)/2)
    brick = Brick(brick_centre_x, current_y, brick_len, brick_width, brick_colors[line_index])
    current_x = brick_centre_x + ((brick_len * 20) / 2) + space
    bricks.append(brick)
    print(len(bricks))
    # if brick_centre_x + ((brick_len * 20) / 2) >= 400:
    if current_x + min(brick_lengths) * 20 / 2 >= end_x:
        current_y = current_y + brick_width * 20 + space
        current_x = -400
        line_index += 1
        print("-----------")

print(len(bricks))

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

    if ball.ycor() <= -215:# ball.distance(paddle) <= 50 and
        ball.bounce_y()
    # elif ball.ycor() <= -215:
    #     print("Game Over")
    #     break

    for brick_obj in bricks:
        size = brick_obj.shapesize()
        length = size[1]
        half_height = length * 20 / 2
        if (
                brick_obj.xcor() - full_half_width - brick_space_half < ball.xcor() < brick_obj.xcor() + full_half_width + brick_space_half and
                brick_obj.ycor() - half_height - space_btw_lines_half < ball.ycor() < brick_obj.ycor() + half_height + space_btw_lines_half):
            # Determine which direction the collision occurred from
            print("hoi")
            score += 1
            label_score.clear()  # Clear the previous text
            label_score.write(score, align="center", font=("Arial", 18, "normal"))

            if abs(ball.xcor() - brick_obj.xcor()) > abs(ball.ycor() - brick_obj.ycor()):
                ball.bounce_x()
            else:
                ball.bounce_y()
            brick_obj.hideturtle()
            bricks.remove(brick_obj)

        if not bricks:
            label_won = turtle.Turtle()
            label_won.hideturtle()
            label_won.color("white")
            label_won.penup()
            label_won.goto(0, 0)
            label_won.write("YOU WON!", align="center", font=("Arial", 24, "normal"))

        # print(len(bricks))
