# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

#-----game configuration----
spot_color="maroon"
spot_size=2
spot_shape="circle"

#-----initialize turtles-----
spot=trtl.Turtle()
spot.shape(spot_shape)
spot.fillcolor(spot_color)
spot.shapesize(spot_size)

#-----game functions--------


#-----events----------------
wn=trtl.Screen()
wn.mainloop()
