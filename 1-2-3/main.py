#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----

apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
fall_speed = int(input("Enter fall speed as a number: "))
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
current_letters = []


#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(apple):
  apple.shape(apple_image)
  current_letters.append(letters.pop(rand.randint(0, len(letters)-1)))
  apple.goto(rand.randint(-150, 150), rand.randint(0, 100))
  apple.showturtle()
  apple.color("white")
  apple.write(current_letters, font=("Arial", 20, "bold"))
  wn.update()

def apple_gravity():
  apple_x = (apple.xcor())
  apple_y = (apple.ycor())
  apple.setheading(270)

  while apple_y > -200:
    apple.clear()
    apple_y -= fall_speed
    apple.goto(apple_x, apple_y)
    apple.write(rand.choice(current_letters), font=("Arial", 20, "bold"))

  apple.hideturtle()
  apple.clear()
  draw_apple(apple)

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_b():
  if "b" in current_letters:
    apple_gravity()
    current_letters.remove("b")

def check_c():
  if "c" in current_letters:
    apple_gravity()
    current_letters.remove("c")

def check_d():
  if "d" in current_letters:
    apple_gravity()
    current_letters.remove("d")

def check_e():
  if "e" in current_letters:
    apple_gravity()
    current_letters.remove("e")

def check_f():
  if "f" in current_letters:
    apple_gravity()
    current_letters.remove("f")

def check_g():
  if "g" in current_letters:
    apple_gravity()
    current_letters.remove("g")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_h():
  if "h" in current_letters:
    apple_gravity()
    current_letters.remove("h")

def check_a():
  if "i" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a"

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

def check_a():
  if "a" in current_letters:
    apple_gravity()
    current_letters.remove("a")

#-----function calls-----

draw_apple(apple)
wn.onkeypress(check_a, "a")
wn.listen()
wn.mainloop()
