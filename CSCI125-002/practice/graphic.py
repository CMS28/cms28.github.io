import turtle

win = turtle.Screen() #get the playground
mypen = turtle.Turtle() # one object
pen2 = turtle.Turtle() # another

# Action
'''
for i in range(100,8,-2):
    mypen.forward(i)
    mypen.left(90)
mypen.forward(100)
'''
# keep moving until the right edge of the screen
x = mypen.xcor()
while x< win.window_width()/2-50:
    mypen.penup()
    mypen.forward(5)
    mypen.pendown()
    x= mypen.xcor()



# wait for close
win.mainloop()
