import turtle

cb = turtle
cb.speed(0)  ##turtle speed control
cb.color('green')  ## turtle color control
cb.turtlesize(1.5, 1.5, 0)  ## turtle size control (width, length, outline)


def draw_circle():
    for i in range(4000):
        cb.forward(i * 0.001)
        cb.left(1)

print(draw_circle())
