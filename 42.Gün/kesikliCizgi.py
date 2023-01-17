import turtle as turtle

tim = turtle.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


# penup() ve pendown() metotları ile kalemi kaldırıp bırakıyoruz.
# penup() metodu ile kalemi kaldırıyoruz.
# pendown() metodu ile kalemi bırakıyoruz.