import turtle
import time
import random

wn=turtle.Screen()
wn.title("Tetris game by sonal")
wn.bgcolor("white")
wn.setup(width=600,height=800)
wn.tracer(0)

delay=0.02

class Shape():
    def __init__(self):
        self.x=5
        self.y=0
        self.color=random.randint(1,7)

        #Block shape
        square=[[1,1],
                    [1,1]]

        horizontal_line = [[1, 1,1,1]]
        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]
        left_l= [[1, 0,0,0],
                  [1, 1,1,1]]

        right_l = [[0, 0, 0, 1],
                  [1, 1, 1, 1]]
        
        left_s=[[1,1,0],
                [0,1,1]]
        
        right_s=[[0,1,1],
                 [1,1,0]]

        t1=[[0,1,0],
           [1,1,1]]

        t2 = [[1, 1, 1],
              [0, 1, 0]]

        shapes=[square,horizontal_line,vertical_line,left_l,right_l,left_s,right_s,t1,t2]
        #choose a random shape each time
        self.shape=random.choice(shapes)

        self.height=len(self.shape)
        self.width=len(self.shape[0])

    def move_left(self,grid):
        if self.x>0:
            if grid[self.y][self.x-1]==0:
                self.erase_shape(grid)
                self.x-=1

    def move_right(self,grid):
        if self.x<12-self.width:
            if grid[self.y][self.x+self.width]==0:
                self.erase_shape(grid)
                self.x+=1

    def draw_shape(self,grid):
        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x] == 1):
                    grid[self.y+y][shape.x+x]=self.color

    def erase_shape(self,grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y+y][shape.x+x]=0

    def can_move(self,grid):
        result=True
        for x in range(self.width):
            if(self.shape[self.height-1][x]==1):
                if(grid[self.y+self.height][self.x+x]!=0):
                    result=False

        return result

    def rotate(self,grid):
        #first erase previous shape
        self.erase_shape(grid)
        rotated_shape=[]
        for x in range(len(self.shape[0])):
            new_row=[]
            for y in range(len(self.shape)-1,-1,-1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)

        right_side=self.x+len(rotated_shape[0])
        if right_side<len(grid[0]):
            self.shape = rotated_shape
            # update the height and width
            self.height = len(self.shape)
            self.width = len(self.shape[0])


grid=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#create the drawing pen
pen=turtle.Turtle()
pen.penup()
pen.speed(1)
pen.shape("square")
pen.setundobuffer(None)

def draw_grid(pen,grid):
    pen.clear()
    top=230
    left=-110

    colors=["black","lightblue","blue","orange","yellow","green","purple","red"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x=left+(x*20)
            screen_y=top-(y*20)
            color_number=grid[y][x]
            color=colors[color_number]
            pen.color(color)
            pen.goto(screen_x,screen_y)
            pen.stamp()

def check_grid(grid):
    #check if each row is full
    y=23
    while y>0:
        is_full=True
        for x in range(0,12):
            if grid[y][x]==0:
                is_full=False
                y-=1
                break
        if is_full:
            global score
            score+=10
            draw_score(pen,score)
            for copy_y in range(y,0,-1):
                for copy_x in range(0,12):
                    grid[copy_y][copy_x]=grid[copy_y-1][copy_x]

def draw_score(pen,score):
    pen.hideturtle()
    pen.goto(-75,250)
    pen.write("Score: {}".format(score),move=False,align="left",font=("Arial",24,"normal"))
    pen.showturtle()

#create the basic shape for the start of the game
shape=Shape()

#put the shape in grid
grid[shape.y][shape.x]=shape.color

#draw the initial grid
#draw_grid(pen,grid)

wn.listen()
wn.onkeypress(lambda : shape.move_left(grid),"Left")
wn.onkeypress(lambda : shape.move_right(grid),"Right")
wn.onkeypress(lambda : shape.rotate(grid),"Up")

score=0
#draw_score(pen,score)

#main game loop
while True:
    wn.update()
    #move the shape
    #Open row
    #check for bottom
    if shape.y==23 - shape.height+1:
        shape=Shape()
        check_grid(grid)
    #check for collision with next row
    elif shape.can_move(grid):
        #erase the current shape
        shape.erase_shape(grid)
        #move the shape by 1
        shape.y+=1
        #draw the shape again
        shape.draw_shape(grid)


    else:
        shape=Shape()
        check_grid(grid)

    #draw the screen
    draw_score(pen,score)
    draw_grid(pen, grid)

    time.sleep(delay)
wn.mainloop()