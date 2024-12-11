# Breakout

# Imports
import turtle as t
import random as rd

#-----Initialize Variables-----
score = 0
player_name = input("Input your name: ")

wn = t.Screen()
wn.colormode(255)

wn.bgcolor('white')

ball = t.Turtle()
#ball.shape('circle')
ball.color(rd.randint(50,255),rd.randint(50,255),rd.randint(50,255))
ball.setheading(45)
ball.speed(3)
ball.penup()


paddle = t.Turtle()
paddle.speed('fastest')
paddle.goto(0,100)

#-----functions-----
def bounce_wall():
    if ball.heading() == 45:
        ball.left(90)
        print('bounce')
    elif ball.heading() == 135:
        ball.right(90)
    elif ball.heading() == 225:
        ball.left(90)
    elif ball.heading() == 315:
        ball.right(90)
def bounce_ceiling():
    if ball.heading == 45 or ball.heading == 135:
        ball.left(180)

def loser():
    wn.mainloop()
def winner():
    print("yay")

#-----events-----
while True:
    ball.forward(2)
    if ball.ycor() <= paddle.ycor():
        #loser()
        paddle.goto(0,150)
    elif ball.xcor() >= -150 or ball.xcor() >= 150:
        bounce_wall()
    elif ball.ycor() >= 150:
        bounce_ceiling()

