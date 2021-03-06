import turtle
import os
import math
import random
import winsound

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")
wn.bgpic("space_invaders_background.gif")

#register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#draw board
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#score
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,250)
scorestring="Score: %s"%score
score_pen.write(scorestring,False,align="Left",font=("Arial",14,"normal"))
score_pen.hideturtle()

#create the player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed=15

enemyspeed=2

#choose a number of enemies
number_of_enemies=5
enemies=[]
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    # create the enemy
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)

#create the players bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bulletspeed=20

#define bullet state
#ready-ready to fire
#fire-bullet is firing
bulletstate="ready"

#move the player
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed
    if x > +280:
        x = +280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as final
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        #move the bullet to above the player
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False

#keyboard bindings
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(fire_bullet,"space")
#main game loop
while True:
    for enemy in enemies:
        #move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #move enemy back and down
        if enemy.xcor()>280:
            #move all enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        if enemy.xcor()<- 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        # check if bullet collision with enemy
        if isCollision(bullet, enemy):
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            x=random.randint(-200,200)
            y = random.randint(100, 250)
            enemy.setposition(x,y)
            #update score
            score+=10
            scorestring="Score:%s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="Left", font=("Arial", 20, "normal"))

        # check if player collision with enemy
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game over!!!")
            break

    #move the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #check if bullet hs gone to top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"

wn.mainloop()
