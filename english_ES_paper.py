import turtle as t
import sys

t.speed('fastest')
t.bgcolor('white')
t.pencolor('grey')
t.pensize(1)
y_start = 440
x_start = -758

def draw_line(x, y, y_step):
    for a in range(0, 6):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(0 - x, y)
        y = y - y_step

def draw_angle(x, x_step, y, y_step):
    for a in range(0, 35):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x - y_step * 5, y - y_step * 5)
        x = x + x_step


print(len(sys.argv)) # argument to indicate the line count

if len(sys.argv) == 2:
    line_count = int(sys.argv[1])
else:
    line_count = 8

y_step = 2 * y_start / (line_count * 7) 
x_step = y_step * 3

for a in range(0, line_count):
    draw_line(x_start, y_start, y_step)
    draw_angle(x_start, x_step, y_start, y_step)
    y_start = y_start - (y_step * 7)

t.hideturtle()

    
    
