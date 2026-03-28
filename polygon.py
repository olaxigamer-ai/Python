import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(600,600)
poly=turtle.Turtle()
side=6
sidelen=70
angle=360/side
for i in range(side):
    poly.fd(sidelen)
    poly.rt(angle)
turtle.done()