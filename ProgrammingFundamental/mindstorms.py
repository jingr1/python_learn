import turtle
def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("gray")
    angie.circle(100)
def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape("turtle")
    triangle.color("yellow")
    for i in range(0,3):
        triangle.backward(100)
        triangle.left(120)
def draw_squares():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
def main():
    window = turtle.Screen()
    window.bgcolor("red")  
    #draw_square()
    #draw_circle()
    #draw_triangle()
    draw_squares()
    window.exitonclick()
main()
