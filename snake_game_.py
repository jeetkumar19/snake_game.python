import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []

# Screen
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("light green")
s1.setup(width=800, height=600)
s1.tracer(0)

# Snake head
h1 = turtle.Turtle()
h1.shape("square")
h1.color("black")
h1.penup()
h1.goto(0, 0)
h1.direction = "stop"

# Food
f1 = turtle.Turtle()
f1.shape("circle")
f1.color("red")
f1.penup()
f1.goto(0, 100)

# Scoreboard
s2 = turtle.Turtle()
s2.speed(0)
s2.color("black")
s2.penup()
s2.hideturtle()
s2.goto(-280, 260)
s2.write("Score: 0  High Score: 0", align="left")

# Movement functions
def move():
    if h1.direction == "up":
        h1.sety(h1.ycor() + 20)
    if h1.direction == "down":
        h1.sety(h1.ycor() - 20)
    if h1.direction == "left":
        h1.setx(h1.xcor() - 20)
    if h1.direction == "right":
        h1.setx(h1.xcor() + 20)

def moveup():
    if h1.direction != "down":
        h1.direction = "up"

def movedown():
    if h1.direction != "up":
        h1.direction = "down"

def moveleft():
    if h1.direction != "right":
        h1.direction = "left"

def moveright():
    if h1.direction != "left":
        h1.direction = "right"

def movestop():
    h1.direction = "stop"


# Keyboard binding
s1.listen()
s1.onkey(moveup, "Up")
s1.onkey(movedown, "Down")
s1.onkey(moveleft, "Left")
s1.onkey(moveright, "Right")
s1.onkey(movestop, "space")

# Main loop
while True:
    s1.update()

    # Border wrap
    if h1.xcor() > 390:
        h1.setx(-390)
    if h1.xcor() < -390:
        h1.setx(390)
    if h1.ycor() > 290:
        h1.sety(-290)
    if h1.ycor() < -290:
        h1.sety(290)

    # Eat food
    if h1.distance(f1) < 20:
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        f1.goto(x, y)

        # Add body part
        b1 = turtle.Turtle()
        b1.speed(0)
        b1.shape("square")
        b1.color("yellow")
        b1.penup()
        bodies.append(b1)

        # Increase score
        sc += 10
        if sc > hs:
            hs = sc

        s2.clear()
        s2.write(f"Score: {sc}  High Score: {hs}", align="left")

        delay = max(0.02, delay - 0.001)

    # Move body
    for i in range(len(bodies)-1, 0, -1):
        bodies[i].goto(bodies[i-1].xcor(), bodies[i-1].ycor())

    if len(bodies) > 0:
        bodies[0].goto(h1.xcor(), h1.ycor())

    move()

    # Check collision with body
    for b in bodies:
        if b.distance(h1) < 20:
            time.sleep(1)
            h1.goto(0, 0)
            h1.direction = "stop"

            for b in bodies:
                b.hideturtle()

            bodies.clear()

            sc = 0
            s2.clear()
            s2.write(f"Score: {sc}  High Score: {hs}", align="left")

            delay = 0.1

    time.sleep(delay)

turtle.done()
