import turtle
import random

# WINDOW
wn = turtle.Screen()
wn.title("BREAKOUT Game!")
wn.bgcolor("#FFC7EA")  # Choose your own color
wn.setup(width=800, height=600)
wn.tracer(0)

# PADDLE
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("#3B0944")  # Choose your own color
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# BALL
ball = turtle.Turtle()
ball.speed(5)
ball.shape("circle")
ball.color("#86003C")  # Choose your own color
ball.penup()
ball.goto(0, -230)
ball.dx = 0.7
ball.dy = -0.7

# BRICKS
bricks = []
brick_colors = ["#4158A6", "#921A40", "#201E43", "#1A5319", "#06D001", "#050C9C", "#FFFF80", "#640D6B"]  # Choose your
# own colors if you'd like
num_rows = 6
num_cols = 10
total_bricks = 30
brick_width = 70
brick_height = 30
horizontal_spacing = (800 - (num_cols * brick_width)) / (num_cols + 1)
vertical_spacing = 20
start_x = -375
start_y = 250

# BRICKS DISPLAY
for row in range(num_rows):
    for col in range(num_cols):
        if len(bricks) < total_bricks:
            brick = turtle.Turtle()
            brick.speed(0)
            brick.shape("square")
            brick.color(random.choice(brick_colors))
            brick.penup()
            x = start_x + col * (brick_width + horizontal_spacing)
            y = start_y - row * (brick_height + vertical_spacing)
            brick.goto(x, y)
            bricks.append(brick)

score = 0
lives = 5
highscore = 0

# SCORE
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")  # Choose your own color
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 270)


def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}  Highscore: {highscore}  Lives: {lives}", align="center",
                        font=("Courier", 15, "normal"))


update_score_display()


def paddle_right():
    if not game_over:
        x = paddle.xcor()
        if x < 350:
            x += 20
            paddle.setx(x)


def paddle_left():
    if not game_over:
        x = paddle.xcor()
        if x > -350:
            x -= 20
            paddle.setx(x)


wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

game_over = False

while True:
    if not game_over:
        wn.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.xcor() > 390:
            ball.setx(390)
            ball.dx *= -1

        if ball.xcor() < -390:
            ball.setx(-390)
            ball.dx *= -1

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.goto(0, -230)
            ball.dy *= -1
            lives -= 1
            update_score_display()
            if lives == 0:
                score_display.clear()
                score_display.write("Oops...you missed! Game over!!!", align="center", font=("Courier", 36, "bold"))
                ball.dx = 0
                ball.dy = 0
                paddle.hideturtle()
                game_over = True
                break

        if (-240 < ball.ycor() < -230) and (
                paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
            ball.sety(-230)
            ball.dy *= -1.1

        for brick in bricks:
            if (brick.ycor() - 15 < ball.ycor() < brick.ycor() + 15) and (
                    brick.xcor() - 35 < ball.xcor() < brick.xcor() + 35):
                ball.dy *= -1
                brick.hideturtle()
                bricks.remove(brick)
                score += 10
                update_score_display()
                if not bricks:
                    score_display.clear()
                    score_display.write("Congratulations! You Win!", align="center", font=("Courier", 36, "bold"))
                    if score > highscore:
                        highscore = score
                    ball.dx = 0
                    ball.dy = 0
                    paddle.hideturtle()
                    game_over = True
                    break
    else:
        ball.dx = 0
        ball.dy = 0
        paddle.hideturtle()