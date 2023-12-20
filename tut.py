import turtle as t
'''
t.shape("square")
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.begin_fill()
t.color("red")
t.circle(100)
'''
t.end_fill()
t.pensize(10)
for angle in range(0,360,30):
    t.seth(angle)
    t.color("red")
    t.circle(100)
t.exitonclick()
