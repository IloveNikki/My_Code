import turtle as t
c=["red","orange","yellow","green","blue","purple"]
t.speed(10)
t.pensize(30)
for i in range(7):
    t.penup()
    t.goto(-150+i*30,0)
    t.setheading(90)
    t.color(c[i])
    t.pendown()
    t.circle(-300+i*30,180)
