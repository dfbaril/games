import turtle
# pong game
wn = turtle.Screen()
wn.title("Neverending turtle Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#scoring
score_1 = 0
score_2 = 0
penScore = turtle.Turtle()
penScore.speed(0)
penScore.color("white")
penScore.penup()
penScore.hideturtle()
penScore.goto(0, 260)
penScore.write("Player 1 : {}  Player 2 : {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal")) 

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

#keybinds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#main game loop
while True:
    wn.update()

    #ballmovement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        penScore.clear()
        penScore.write("Player 1 : {}  Player 2 : {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal")) 
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        penScore.clear()
        penScore.write("Player 1 : {}  Player 2 : {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal")) 
    if ball.xcor() > 390 and ball.xcor() < -390:
        ball.dx += 0.15
        ball.dy += 0.15

    #paddle and ball collision 
    if ball.xcor() > 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1