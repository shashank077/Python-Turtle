import turtle
def draw_square():
    window=turtle.Screen()
    window.bgcolor("Yellow")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("Black")
    brad.speed(1.5)
    i=0
    while i<4:
     brad.forward(100)
     brad.right(90)
     i+=1
def draw_circle():
    window = turtle.Screen()
    window.bgcolor("Yellow")
    angle=turtle.Turtle()
    angle.shape("turtle")
    angle.color("Blue")
    angle.circle(100)
    window.exitonclick()
def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("Yellow")
    amy=turtle.Turtle()
    amy.shape("arrow")
    amy.color("Green")
    i=0
    while i<3:
     amy.right(120)
     amy.forward(200)
     i+=1
    window.exitonclick()

k=input("Enter 1 for square 2 for cirle and 3 for trianle")
if k=='1':
    draw_square()
elif k=='2':
    draw_circle()
elif k=='3':
    draw_triangle()
else:
    print("INVALID")


