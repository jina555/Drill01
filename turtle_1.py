import turtle

def move_w():
    turtle.forward(50)
    turtle.stamp()

def move_a():
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()

def move_d():
    turtle.right(90)
    turtle.forward(50)
    turtle.stamp()

def move_s():
    turtle.backward(50)
    turtle.stamp()

turtle.shape('turtle')

turtle.onkey(move_w, 'w')
turtle.onkey(move_a, 'a')
turtle.onkey(move_d, 'd')
turtle.onkey(move_s, 's')

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(restart,'Escape')
turtle.listen()

turtle.exitonclick()