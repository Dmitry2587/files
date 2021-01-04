from turtle import Turtle
from itertools import cycle


elements = ['Java', 'Python', 'C++', 'Python']
elements_percentage = {('Java', 25), ('Python', 50), ('C++', 25)}
COLORS = cycle(['yellow', 'green', 'red', 'cyan', 'white', 'blue'])
radius = 175

# This will draw a pie chart

total = sum(element for _, element in elements_percentage)

pie = Turtle()
pie.penup()
pie.sety(-radius)
pie.pendown()

def make_pie_chart():
    for _, element in elements_percentage:
        pie.fillcolor(next(COLORS))
        pie.begin_fill()
        pie.circle(radius, element * 360 / total)
        position = pie.position()
        pie.goto(0, 0)
        pie.end_fill()
        pie.setposition(position)

print(make_pie_chart())


# This will make a legend to a graph



pie.hideturtle()
