import turtle
import random

score=0
lives=5

wn=turtle.Screen()
wn.title("Falling skies")
wn.bgcolor("green")
wn.setup(width=800,height=600)
wn.tracer(0)

#Add the player
player=turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction="stop"

#create a list of good guys
good_guys=[]

#add the good_guy
for _ in range(20):
    good_guy=turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100,250)
    good_guy.speed=random.randint(1,4)
    good_guys.append(good_guy)

#create a list of bad guys
bad_guys=[]

#add the bad_guy
for _ in range(20):
    bad_guy=turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("circle")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100,250)
    bad_guy.speed=random.randint(1,4)
    bad_guys.append(bad_guy)

#create a pen
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("Score: {} Lives: {}".format(score,lives),align="center",font=("Courier",24,"normal"))

#functions
def go_left():
    player.direction="left"

def go_right():
    player.direction="right"

#keyboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#main game loop
while True:
    #update screen
    wn.update()

    #move the player
    if player.direction=="left":
        x=player.xcor()
        x-=3
        player.setx(x)

    if player.direction=="right":
        x=player.xcor()
        x+=3
        player.setx(x)

    #move the good guy
    for good_guy in good_guys:
        y=good_guy.ycor()
        y-=good_guy.speed
        good_guy.sety(y)

        #check if off the screen
        if y<-300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            good_guy.goto(x,y)

        #check for collision with player
        if good_guy.distance(player)<20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score +=10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    # move the bad guy
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        # check for collision with player
        if bad_guy.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score-=10
            lives-=1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    if(lives==0):
        player.hideturtle()
        wn.bye()

wn.mainloop()