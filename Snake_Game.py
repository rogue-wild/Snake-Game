#Experimental snake game in python programming language for Windows Operating System...

import turtle
import time
import random
score = 0
high_score = 0

delay = 0.1

wn = turtle.Screen()
#title and credits...
wn.title("Snake  o---------o Game by Rogue-Wild")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

segment = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0 ; High Score : 0", align = "center", font =( "Courier", 24 , "normal"))

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "move"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("light green")
food.penup()
food.goto(100,100)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

wn.listen()
#registering movement by user inputs...
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for seg in segment:
            seg.goto(1000,1000)
        segment.clear()

        score = 0
        pen.clear()
        pen.write("Score : {} ; High Score : {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segment.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} ; High Score : {}".format(score, high_score), align = "center", font =( "Courier", 24 , "normal"))

    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)

    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    move()

    for seg in segment:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for seg in segment:
                seg.goto(1000, 1000)

            segment.clear()

    time.sleep(delay)

wn.mainloop()
