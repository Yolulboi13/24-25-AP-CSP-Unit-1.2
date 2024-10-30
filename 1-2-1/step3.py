# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rd

#-----game configuration----
spot_color="maroon"
spot_size=2
spot_shape="circle"

global score
score=0

font_setup=("Arial", 20, "normal")

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtles-----
spot=trtl.Turtle()
spot.shape(spot_shape)
spot.fillcolor(spot_color)
spot.shapesize(spot_size)
spot.penup()
spot.speed("fastest")

writer=trtl.Turtle()
writer.penup()
writer.goto(-450, 350)

counter=trtl.Turtle()
counter.penup()
counter.goto(-450,-350)

#-----game functions--------
def spot_clicked(x, y):
    change_position()
    score_update()

def change_position():
    new_x = rd.randint(-400,400)
    new_y = rd.randint(-300,300)
    spot.hideturtle()
    spot.goto(new_x,new_y)
    spot.showturtle()

def score_update():
    global score
    score+=1
    writer.clear()
    writer.write(("Score: "+str(score)), font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    spot.hideturtle()
    spot.goto(-99999, 99999)
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
spot.onclick(spot_clicked)

wn=trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            