import turtle


bug = turtle
bug.setheading(90)

for a in range(150, 0, -5):
    bug.fd(a)
    bug.right(90)
    print(a)
