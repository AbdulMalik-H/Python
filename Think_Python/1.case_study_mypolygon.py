import turtle
import math


def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circul(t,r):
    arc(t,r,360)

def arc(t, r, angle):
    arc_lenght= 2 * math.pi * r * angle/360
    n = int(arc_lenght/3)
    step_length = arc_lenght/n
    step_angle= float(angle)/n
    polyline(t, n, step_length, step_angle)

bob = turtle.Turtle()

polygon(t=bob, n=5, length=50)
circul(t=bob, r=100)
arc(t=bob, r=200, angle=90)
turtle.mainloop()