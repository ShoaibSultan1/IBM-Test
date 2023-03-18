import turtle 

turtle.speed(3)
turtle.bgcolor("black")
turtle.pensize(3)
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('red','pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()

# time=(13)

# if time<12:
#     print("good morning")

# else:
#     print("good evening")

# a = int(input("Enter any value between 1 and 9 : "))

# if (a<1 or a>9):
#     raise ValueError("Value should be between 1 and 9")
