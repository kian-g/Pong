#Imports

import turtle

################################################################################

wn = turtle.Screen()
wn.title("Pong!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
scoreA = 0
scoreB = 0

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)


#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = .15 #CHANGE THESE NUMBERS TO ADJUST THE BALL SPEED! FRom 0.1 - 10
ball.dy = .15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

#Funcs (def)
def paddleAUp():
    y = paddleA.ycor()
    y += 30
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 30
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += 30
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 30
    paddleB.sety(y)
#Keyboard Binding
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDown, "Down")
#Main game loop

while True:
    wn.update()

    #MOve BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))


    #Paddle + ball bouse
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
