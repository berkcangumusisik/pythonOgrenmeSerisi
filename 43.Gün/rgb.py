import turtle as t
import random 

tim = t.Turtle()
t.colormode(255) #.colormode() fonksiyonu ile renklerin 0-255 arasında olmasını sağladık.

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

directions = [0,90,180,270]
tim.pensize(15) #.pensize() fonksiyonu ile tim'in kalem kalınlığını ayarladık.
tim.speed("fastest") #.speed() fonksiyonu ile tim'in hızını ayarladık.

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))