import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Maze game by sonal")
wn.setup(700,700)
wn.tracer(0)


#register shapes
#turtle.register_shape("wizard_right.gif")
#turtle.register_shape("wizard_left.gif")
#turtle.register_shape("treasure.gif")
#turtle.register_shape("wall.gif")


#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#create player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0

    def go_up(self):
        #calculate the spot to move to
        move_to_x=self.xcor()
        move_to_y = self.ycor()+24
        #check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def go_down(self):
        # calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        # check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def go_left(self):
        # calculate the spot to move to
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        # check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def go_right(self):
        # calculate the spot to move to
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        # check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b = self.ycor() - other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<5:
            return True
        else:
            return False

#create treasure
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
    def move(self):
        if self.direction=="up":
            dx=0
            dy=24
        elif self.direction=="down":
            dx=0
            dy=-24
        elif self.direction=="left":
            dx=-24
            dy=0
        elif self.direction=="right":
            dx=24
            dy=0
        else:
            dx=0
            dy=0

        #check if player is close
        #if so go in that direction
      #  if self.is_close(player):
       #     if player.xcor()<self.xcor():
        #        self.direction="left"
         #   elif player.xcor()>self.xcor():
          #      self.direction="right"
           # elif player.ycor()<self.ycor():
           #     self.direction="down"
          #  elif player.ycor()>self.ycor():
           #     self.direction="up"

        # calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        # check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction=random.choice(["up","down","left","right"])

        #set timmer to move next time
        turtle.ontimer(self.move,t=random.randint(100,300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#create levels list
levels=[""]

#define first level
level_1=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXE         XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX       EXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"XT XXX        XXXXT XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXXE                    X",
"XXXT        XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XXT  XXXXX             TX",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXXE                   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#add a treasure list
treasures=[]

#add a enemies list
enemies=[]

# add maze to maze list
levels.append(level_1)

#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get the character at each x,y coordinate
            #note the order of y and x in the next line
            character=level[y][x]
            #calculate the screen x,y coordinates
            screen_x=-288+(x*24)
            screen_y=288-(y*24)

            #check if it is a x (representing a wall)
            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                #add coordinates to wall list
                walls.append((screen_x,screen_y))
            # check if it is a P (representing a wall)
            if character == "P":
                player.goto(screen_x, screen_y)

            # check if it is a E (representing a wall)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            # check if it is a T (representing a wall)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))


#create class instances
pen=Pen()
player=Player()

#create wall coordinate list
walls=[]

#set up the levels
setup_maze(levels[1])

#keyboard binding
wn.listen()
wn.onkeypress(player.go_left,"Left")
wn.onkeypress(player.go_right,"Right")
wn.onkeypress(player.go_up,"Up")
wn.onkeypress(player.go_down,"Down")

# turn of screen updates
wn.tracer(0)

#start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)

#main game loop
while True:
    #check for player collision with treasure
    #iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #add the treasure gold to the player gold
            player.gold+=treasure.gold
            print("Player Gold:{}",format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("player dies!")
            player.goto(-288+24,288-24)
    wn.update()