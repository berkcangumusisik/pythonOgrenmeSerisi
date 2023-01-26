from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(30)
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear() # .clear() ile ekranı temizliyoruz.
    tim.penup() # .penup() ile kalemi kaldırıyoruz.
    tim.home() #.home() ile konumu başlangıç noktasına getiriyoruz.
    tim.pendown()
screen.listen() #.listen() ile klavyeden gelen inputları dinliyoruz.
screen.onkey(move_forward,"w") #.onkey() ile klavyeden gelen inputları fonksiyonlara bağlıyoruz.
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()