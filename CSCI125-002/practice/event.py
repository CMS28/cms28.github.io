import turtle
wn = turtle.Screen()
me = turtle.Turtle()
#me.color("red")
# action -- function go up
def goup():
    me.seth(90)
    me.forward(50)
def goleft():
    me.seth(180)
    my.forward(50)
def gored():
    me.color("red")
# binding
wn.onkey(goup,"Up")
wn.onkey(goleft,"Left")
wn.onkey(gored,"R")
#listen
wn.listen()

#keep going
wn.mainloop()