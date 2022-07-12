import turtle as t
import sys

t.speed('fastest')
t.bgcolor('white')
t.pencolor('light grey')
t.pensize(1)
y_start = 440
x_start = -758
CTG50 = 0.839

def draw_line(x, y, y_step):
    for a in range(0, 6):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(0 - x, y)
        offset = 0
        if a == 1 or a == 3 or a == 4:
            t.pencolor('hot pink')
            if a == 1:
                offset = y - y_step / 3
            elif a == 3:
                offset = y - y_step / 5
            elif a == 4:
                offset = y - y_step / 2.3
            t.penup()
            t.goto(x, offset)
            t.pendown()
            t.goto(0 - x, offset)
        y = y - y_step
        t.pencolor('light grey')

def draw_angle(x, x_step, y, y_step):
    t.pencolor('light grey')
    for a in range(0, 35):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x - y_step * 5 * CTG50, y - y_step * 5)
        x = x + x_step


print(len(sys.argv)) 

if len(sys.argv) == 2:
    line_count = int(sys.argv[1])
else:
    line_count = 7

y_step = 2 * y_start / (line_count * 7) 
x_step = y_step * 3

for a in range(0, line_count):
    draw_line(x_start, y_start, y_step)
    draw_angle(x_start, x_step, y_start, y_step)
    y_start = y_start - (y_step * 7)

t.hideturtle()
   
