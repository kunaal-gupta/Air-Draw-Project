import turtle


t = turtle.Turtle()
s = turtle.Screen()
t.speed(1000)
i = 50
t.width(2)
t.pensize(0)
count = 0

while True:
    if count == 5:
        t.clear()
        s.bye()
    else:
        count +=1

        t.forward(2)
        color = ['red', 'blue', 'green', 'black']
        fillcolor = ['orange', 'darkblue', 'darkgreen', 'brown']
        for i in range(4):

            t.begin_fill()
            t.color(color[i], fillcolor[i])
            t.right(90)
            t.circle(110, extent=180)

            t.forward(190)
            t.circle(20, 180)
            t.forward(140)
            t.right(180)

            t.forward(190)
            t.circle(20, 180)
            t.forward(170)
            t.right(180)

            t.forward(185)
            t.circle(20, 180)
            t.forward(185)
            t.right(180)

            t.forward(150)
            t.circle(20, 180)
            t.forward(170)
            t.right(180)
            t.end_fill()

