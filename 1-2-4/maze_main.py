import turtle as t
import random as rd
# Initialize Variables

wn = t.Screen()
wn.listen()

pen = t.Turtle()
pen.speed(0)
pen.color('black')
pen.pensize(2)
pen.setheading(90)

length = 10
path_width = 20
maze_size = rd.randint(20,40)

# Draws the initial walls
for num in range(maze_size):
    pen.forward(length)
    pen.left(90)
    length += 10

# Draws the gaps in the maze
def draw_doors():
    length = 10
    for num in range(maze_size):
        chance = rd.randint(1, 2)
        if chance == 1:
            distance = rd.randint(0,length)
            pen.forward(distance)
            pen.color('white')
            pen.forward(path_width)
            pen.color('black')
            pen.forward(length-distance-path_width)
        elif chance == 2:
            pen.forward(length)
        pen.left(90)
        length += 10

# Adds barriers in the wall
def draw_barriers():
    length = 10
    for num in range(maze_size):
        if num > rd.randint(5,10):
            chance = rd.randint(1, 2)
            if chance == 1:
                pen.penup()
                distance = rd.randint(0, length)
                pen.forward(distance)
                pen.pendown()
                pen.right(90)
                pen.forward(path_width)
                pen.backward(path_width)
                pen.left(90)
                pen.forward(length-distance)
            elif chance == 2:
                pen.forward(length)
            pen.left(90)
            length += 10
        else:
            pen.forward(length)
            pen.left(90)
            length += 10

def return_to_center():
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.pendown()
    pen.color('black')

choice = rd.randint(1, 3)
if choice == 1:
    return_to_center()
    draw_doors()
    return_to_center()
    draw_barriers()
if choice == 2:
    return_to_center()
    draw_barriers()
    return_to_center()
    draw_doors()
if choice == 3:
    return_to_center()
    draw_doors()
    return_to_center()
    draw_barriers()
    return_to_center()
    draw_doors()

wn.mainloop()
