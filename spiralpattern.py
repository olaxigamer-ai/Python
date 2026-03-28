import turtle
mywindow=turtle.Screen()
mywindow.bgcolor("yellow")
turtle.speed(10)
mywindow.title("Spiral Pattern")
mypen=turtle.Turtle()
size=0

while True:
    for i in range(4):
        mypen.fd(size+1)
        mypen.lt(90)
        size=size-5
    size=size+1
turtle.done()