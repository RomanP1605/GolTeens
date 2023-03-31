import turtle

def sq(a):
    for i in range(4):
        square.forward(a)
        square.left(90)
colors=["Orange", "Blue"]
square=turtle.Turtle()
square.speed(100)
a = 100
a += 10
for i in range(10):
    square.color(colors[i%2])
    sq(a)
    square.right(10)
    a += 10