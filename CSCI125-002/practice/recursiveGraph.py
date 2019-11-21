import turtle

win = turtle.Screen()
me = turtle.Turtle()

def recurG(length):
    #base case
    if length <10:
        return
    #general case
    else:
        me.forward(length)
        me.left(90)
        recurG(length-5)
        me.right(20)
        recurG(length/3)


#recurG(200)

def koch(t,order,size):
    #base case
    if order<=0 :
        t.forward(size)
    #general case
    else:
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)
        t.right(120)
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)
#test function
koch(me,3,150)