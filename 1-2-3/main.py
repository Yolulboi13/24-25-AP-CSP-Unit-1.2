#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
fall_speed = int(input("Enter fall speed as a number: "))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_gravity():
  apple_x = (apple.xcor())
  apple_y = (apple.ycor())
  apple.setheading(270)
  while apple_y > -200:
    apple.clear()
    apple_y -= fall_speed
    apple.goto(apple_x, apple_y)
    apple.color("white")
    apple.write("A", font=("Arial", 20, "bold"))


#-----function calls-----
draw_apple(apple)
wn.onkeypress(apple_gravity, "a")
wn.listen()
wn.mainloop()