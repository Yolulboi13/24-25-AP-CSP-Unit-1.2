# Breakout

# Imports
import turtle as t
import random as rd

#-----Initialize Variables-----
score = 0
player_name = input("Input your name: ")
wn = t.Screen()
ball = t.Turtle()
ball_direction = 90
wn.bgcolor('black')
ball.shape('circle')
ball.color(rd.randint(50,255),rd.randint(50,255),rd.randint(50,255))






wn.mainloop()