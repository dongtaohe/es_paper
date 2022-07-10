import turtle as t

t.speed('fastest')
t.bgcolor('white')
t.pencolor('light grey')
t.pensize(1)

def draw_line(y, y_step):
    for a in range(0, 6):
        t.penup()
        t.goto(-700, y)
        t.pendown()
        t.goto(700, y)
        y = y - y_step
        t.penup()

y_start = 440
y_step = 15
for a in range(0, 9):
    draw_line(y_start, y_step)
    y_start = y_start - (y_step * 6 + 10)
   
