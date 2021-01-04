from turtle import Turtle, Screen
from itertools import cycle


elements = ['Java', 'Python', 'C++', 'Python']
unique_elements = list(set(elements))
unique_list_count = [elements.count(language) for language in unique_elements]
percentage = []
for i in unique_list_count:
    percentage.append(i / len(elements) * 100)
total_list_length = len(elements)
colors = cycle(['yellow', 'green', 'red', 'cyan', 'white', 'blue'])
radius = 180
total = sum(element for element in percentage)

# This will draw a pie chart

pie = Turtle()
pie.penup()
pie.sety(-radius)
pie.pendown()


def make_pie_chart():
    for element in percentage:
        pie.fillcolor(next(colors))
        pie.begin_fill()
        pie.circle(radius, element * 360 / total)
        position = pie.position()
        pie.goto(0, 0)
        pie.end_fill()
        pie.setposition(position)


print(make_pie_chart())

# This will make a legend to a graph without colors

pie.up()
pie.goto(300, 300)
pie.write(unique_elements, move=False, align='left')
pie.goto(290, 290)
pie.write(unique_list_count, move=False, align='left')

pie.hideturtle()

screen = Screen()
screen.exitonclick()
