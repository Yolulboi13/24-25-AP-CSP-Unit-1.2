import turtle as trtl
a = trtl.Turtle()
a.speed(0)
step=1
color=input("Choose a color: ")
a.color(color)
while True:
    a.circle(step,step,step)
    step+=1