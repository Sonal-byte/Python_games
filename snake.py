import turtle
import time
import random
delay=0.1

#score
score=0
high_score=0

wn=turtle.Screen()
wn.title("snake game by sonal")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#head
x = random.randint(-290, 290)
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0, High Score: 0",align="center",font=("Courier",24,"normal"))

#function
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

def go_up():
    if head.direction != "down":
        head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"
def go_left():
    if head.direction != "righ":
        head.direction="left"
def go_right():
    if head.direction != "left":
        head.direction="right"

#keyword binding
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


#main game
while True:
    wn.update()

    #collisions with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        # hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # clear the segments
        segments.clear()

        # Reset the score
        score=0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for collisions with the food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290, 290)
        food.goto(x,y)

        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # increase score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))

    #move the end segments first in reverese
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    # move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    # check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments
            segments.clear()
            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)
wn.mainloop()