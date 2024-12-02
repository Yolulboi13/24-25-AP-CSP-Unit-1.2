import turtle as t
# Initialize Variables

wn = t.Screen()
wn.listen()

pen = t.Turtle()
pen.speed('fastest')
pen.color('black')
pen.pensize(2)
pen.setheading(90)

length = 10
path_width = 20

# Draws the inital walls
for num in range(25):
    pen.forward(length)
    pen.left(90)
    length += 10

for num in range(4):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(num * 90)
    pen.pensize(path_width)
    pen.left(25)
    pen.color('white')
    pen.forward(200)

# Adds barriers in the wall
for num in range(4):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(num*90)
    length = 10
    pen.color('black')
    pen.pensize(2)
    for num2 in range(6):
        pen.forward(length/2)
        pen.right(90)
        pen.forward(20)
        pen.left(90)
        length += 10

wn.mainloop()