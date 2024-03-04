# Pong Game 
# By: Prathamesh Chaudhari
# Acknowledgement: Christian Thompson -- FreeCodeCamp 

import turtle

# Display Window
Display = turtle.Screen()
Display.title("Pong By Prathamesh Chaudhari")
Display.bgcolor("Gray")
Display.setup(width = 1000, height = 600)
Display.tracer(0)

# Two Rackets -- Racket 1 & Racket 2

# Racket 1
Racket1 = turtle.Turtle()
Racket1.speed(0)
Racket1.shape("square")
Racket1.shapesize(5,1)
Racket1.color("Black")
Racket1.penup()
Racket1.goto(-400,0)

# Racket 2
Racket2 = turtle.Turtle()
Racket2.speed(0)
Racket2.shape("square")
Racket2.shapesize(5,1)
Racket2.color("Black")
Racket2.penup()
Racket2.goto(400,0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("Black")
Ball.penup()
Ball.goto(0,0)
# Change in the x and y direction of the ball (Change as per your computer speed).
Ball.cx = 0.15 
Ball.cy = 0.15

# Racket Movement
def Racket1_up():
    y_cordinate = Racket1.ycor()
    y_cordinate += 10
    Racket1.sety(y_cordinate)

def Racket1_down():
    y_cordinate = Racket1.ycor()
    y_cordinate -= 10
    Racket1.sety(y_cordinate)

def Racket2_up():
    y_cordinate = Racket2.ycor()
    y_cordinate += 10
    Racket2.sety(y_cordinate)

def Racket2_down():
    y_cordinate = Racket2.ycor()
    y_cordinate -= 10
    Racket2.sety(y_cordinate)

# Key Binding 
Display.listen()
Display.onkeypress(Racket1_up, "w")
Display.onkeypress(Racket1_down, "s")
Display.onkeypress(Racket2_up, "Up")
Display.onkeypress(Racket2_down, "Down")

# Score
PlayerA_Score = 0
PlayerB_Score = 0

# Score Manager
Write = turtle.Turtle()
Write.speed(0)
Write.color("Black")
Write.penup()
Write.hideturtle()
Write.goto(0,260)
Write.write("Player 1: 0    Player 2: 0", align = "center", font = ("Helvetica",15,"normal"))

# Game 
while True:
    Display.update()

    # Ball Movement
    Ball.setx(Ball.xcor() + Ball.cx)
    Ball.sety(Ball.ycor() + Ball.cy)

    # Border
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.cy *= -1 
    
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.cy *= -1 
    
    if Ball.xcor() > 440:
        Ball.goto(0,0)
        Ball.cx *= -1 
        PlayerA_Score += 1
        Write.clear()
        Write.goto(0,260)
        Write.write("Player 1: {}    Player 2: {}".format(PlayerA_Score,PlayerB_Score), PlayerB_Score, align = "center", font = ("Helvetica",15,"normal"))

    if Ball.xcor() < -440:
        Ball.goto(0,0)
        Ball.cx *= -1 
        PlayerB_Score += 1
        Write.clear()
        Write.goto(0,260)
        Write.write("Player 1: {}    Player 2: {}".format(PlayerA_Score,PlayerB_Score), PlayerB_Score, align = "center", font = ("Helvetica",15,"normal"))

# Ball and Racket Collision 
    if (Ball.xcor() > 390 and Ball.xcor() < 400) and (Ball.ycor() < Racket2.ycor() + 40 and Ball.ycor() > Racket2.ycor() - 40):
        Ball.setx(390)
        Ball.cx *= -1

    if (Ball.xcor() < -390 and Ball.xcor() > -400) and (Ball.ycor() < Racket1.ycor() + 40 and Ball.ycor() > Racket1.ycor() - 40):
        Ball.setx(-390)
        Ball.cx *= -1
