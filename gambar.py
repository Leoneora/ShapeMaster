#File "gambar.py" untuk kumpulan def() atau fungsi yang akan menggambar bangun datar dan bangun ruang yang akan dipanggil.
#dibuat oleh E. Keisha P.

from turtle import *

#Gambar bangun datar
def draw_lingkaran():
    pensize(2)
    color("black")
    circle(100)
    exitonclick()

def draw_segitiga():
    pensize(2)
    color("black")
    for i in range(3):
        forward(100)
        left(120)
    exitonclick()

def draw_persegi():
    pensize(2)
    color("black")
    for i in range(4):
        forward(100)
        left(90)
    exitonclick()

def draw_PersegiPanjang():
    pensize(2)
    color("black")
    for i in range(2):
        forward(200)
        left(90)
        forward(100)
        left(90)
    exitonclick()

def draw_trapesium_sama_kaki():
    pensize(2)
    color("black")
    forward(100)
    right(60)
    forward(80)
    right(120)
    forward(180)
    right(120)
    forward(80)
    hideturtle()
    exitonclick()

def draw_trapesium_sikusiku():
    pensize(2)
    forward(100)
    right(60)
    forward(80)
    right(120)
    forward(140)
    right(90)
    forward(70)
    hideturtle()
    exitonclick()

def draw_jajargenjang():
    pensize(2)
    forward(100)
    right(60)
    forward(70)
    right(120)
    forward(70)
    right(120)
    forward(70)
    hideturtle()
    exitonclick()

#Gambar bangun ruang