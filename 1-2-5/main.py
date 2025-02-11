# Breakout

#NOTE: THIS CODE IS ANYTHING BUT COMPLETE, ALTHOUGH I BELIEVE WE AT LEAST MET THE REQUIREMENTS DESPITE IT NOT BEING COMPLETELY FUNCTIONAL OR STABLE

# Imports
import turtle as t
import random as rd

#-----Initialize Variables-----
score = 0
player_name = input("Input your name: ")

# Recommended Values: 250, -100, 100, -51, 2
ceiling_height = 250
left_wall = -100
right_wall = 100
void_pos = -51
ball_speed = 2

# draws the walls that define the space played in
# Initialize wall painter
wall_painter = t.Turtle()
wall_painter.speed(0)
wall_painter.penup()
wall_painter.hideturtle()
wall_painter.color('white')
wall_painter.pensize(2)
# draw walls
wall_painter.goto(left_wall, void_pos)
wall_painter.pendown()
wall_painter.goto(left_wall, ceiling_height)
wall_painter.goto(right_wall, ceiling_height)
wall_painter.goto(right_wall, void_pos)
# making the losing line red
wall_painter.color('red')
wall_painter.goto(left_wall, void_pos)

#  lets us use rgb values on the screen
wn = t.Screen()
wn.colormode(255)

# Sets window color to black
wn.bgcolor('black')

#creates the bouncing ball
ball = t.Turtle()
ball.shape('circle')
ball.color(rd.randint(50,255),rd.randint(50,255),rd.randint(50,255))
ball.setheading(45)
ball.speed(3)
ball.penup()

#makes the paddle that the player controls
paddle = t.Turtle()
paddle.speed(0)
paddle.penup()
paddle.color('white')
paddle.goto(0, void_pos - 1)
paddle.shape('square')

#starts working with the score
score_trtl = t.Turtle()
score_trtl.penup()
score_trtl.speed(0)
score_trtl.color('white')
score_trtl.goto(-300,-200)
score_trtl.hideturtle()

# List of brick coords
brick_coords = [(-80,225),(-60,225),(-40,225),(-20,225),(0,225),(20,225),(40,225),(60,225),(80,225),(-60,175),(-40,175),(-20,175),(0,175),(20,175),(40,175),(60,175),(-40,125),(-20,125),(0,125),(20,125),(40,125)]

brick_break_range_end = 20
# Creates Turtles
brick_1 = t.Turtle()
brick_2 = t.Turtle()
brick_3 = t.Turtle()
brick_4 = t.Turtle()
brick_5 = t.Turtle()
brick_6 = t.Turtle()
brick_7 = t.Turtle()
brick_8 = t.Turtle()
brick_9 = t.Turtle()
brick_10 = t.Turtle()
brick_11 = t.Turtle()
brick_12 = t.Turtle()
brick_13 = t.Turtle()
brick_14 = t.Turtle()
brick_15 = t.Turtle()
brick_16 = t.Turtle()
brick_17 = t.Turtle()
brick_18 = t.Turtle()
brick_19 = t.Turtle()
brick_20 = t.Turtle()
brick_21 = t.Turtle()

# Putting turtles in a list for later access and organization
brick_trtl_list = [brick_1, brick_2, brick_3 , brick_4 , brick_5 , brick_6 , brick_7 , brick_8 , brick_9 , brick_10, brick_11, brick_12, brick_13, brick_14, brick_15, brick_16, brick_17, brick_18, brick_19, brick_20, brick_21]

# Setting up turtles using the list from before
for num in range(21):
    brick_trtl_list[num].color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    brick_trtl_list[num].speed(0)
    brick_trtl_list[num].shape('square')
    brick_trtl_list[num].penup()
    brick_trtl_list[num].goto(brick_coords[num])

#-----functions-----
# function for bouncing off a wall
def bounce_wall():
    # Checks which way to face after bounce
    if ball.heading() == 45:
        ball.left(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 135:
        ball.right(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 225:
        ball.left(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 315:
        ball.right(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))

# bouncing off the ceiling
def bounce_ceiling():
    # headed right or left essentially
    if ball.heading() == 45:
        ball.right(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 135:
        ball.left(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))

# bouncing off the paddle
def bounce_paddle():
    if ball.heading() == 225:
        ball.right(90)
    elif ball.heading() == 315:
        ball.left(90)

# When ball goes below line
def loser():
    print("Sorry, ", player_name,". You only managed to break ", score," bricks..." )
    wn.mainloop()

# When all bricks destoryed
def winner():
    print("Congrats, ", player_name,". You broke all the bricks!!")

# moving paddle functions
def paddle_left():
    paddle.setheading(180)
    paddle.forward(5)
def paddle_right():
    paddle.setheading(0)
    paddle.forward(5)

# increase score function
def score_up_one():
    global score
    score += 1
    score_trtl.clear()
    score_trtl.write("Score: "+str(score), font=("Helvetica", 32, "bold"))

# brick breaking (not quite working)
def brick_broken():
    global brick_break_range_end
    print("brick")
    for num in range(0, brick_break_range_end):
        brick_break_range_end -= 1
        if ball.distance(brick_trtl_list[num]) <= 20:
            brick_trtl_list[num].hideturtle()
            brick_trtl_list[num] = "broken"
    score_up_one()

#-----events-----
while True:
    # Move the ball
    ball.forward(ball_speed)

    # Paddle movement events
    # WASD inputs
    wn.onkeypress(paddle_left, "a")
    wn.onkeypress(paddle_right, "d")
    # Arrow key inputs
    wn.onkeypress(paddle_left, "Left")
    wn.onkeypress(paddle_right, "Right")

    # This is temporary and for testing purposes only
    # wn.onkeypress(score_up_one, "Up")

    # Makes wn look for inputs
    wn.listen()

    # Checking position of ball relative to other things
    # First the walls
    if ball.xcor() <= left_wall or ball.xcor() >= right_wall:
        bounce_wall()

    # Then the ceiling
    if ball.ycor() >= ceiling_height:
        bounce_ceiling()

    # Then the bottom/void
    if ball.ycor() <= void_pos:
        loser()

    # Then Paddle
    if ball.ycor() <= 45:
        if ball.distance(paddle) <= 20:
            bounce_paddle()

    # Then all the bricks
    if ball.distance(brick_trtl_list[0] or brick_trtl_list[1] or brick_trtl_list[2] or brick_trtl_list[3] or brick_trtl_list[4] or brick_trtl_list[5] or brick_trtl_list[6] or brick_trtl_list[7] or brick_trtl_list[8] or brick_trtl_list[9] or brick_trtl_list[10] or brick_trtl_list[11] or brick_trtl_list[12] or brick_trtl_list[13] or brick_trtl_list[14] or brick_trtl_list[15] or brick_trtl_list[16] or brick_trtl_list[17] or brick_trtl_list[18] or brick_trtl_list[19] or brick_trtl_list[20]) <= 20:
        brick_broken()