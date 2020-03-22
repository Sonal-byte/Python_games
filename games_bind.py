from tkinter import *
import subprocess
from tkinter.font import Font
from PIL import ImageTk,Image

wn=Tk()
wn.title("Games")
wn.geometry("700x600")

#image=ImageTk.PhotoImage(Image.open("brown-book-page-1112048.jpg"))
#img_label=Label(image=image)
#img_label.grid()

f = Font(font=("Courier", 30, "bold"))
f1 = Font(font=("Courier", 20, "bold"))

def space_invender_fn(event):
    subprocess.run('python space_invender.py', shell=True)

def snake_fn(event):
    subprocess.run('python snake.py', shell=True)

def tetris_fn(event):
    subprocess.run('python Tetris.py', shell=True)

def maze_fn(event):
    subprocess.run('python maze.py', shell=True)

def pong_fn(event):
    subprocess.run('python pong_game.py', shell=True)

def falling_skies_fn(event):
    subprocess.run('python Falling_skies.py', shell=True)

app=Frame(wn)
app.grid()
label=Label(app,text="Welcome to Python Games",font=f,pady=10)
label.grid(column=0,row=0)

label1=Label(app,text="")
label1.grid(column=0,row=1)

space_invender=Button(app,text="Space Invender",font=f1,pady=10)
space_invender.grid(column=0,row=2)
space_invender.bind("<Button-1>",space_invender_fn)

label2=Label(app,text="")
label2.grid(column=0,row=3)

snake=Button(app,text="Snake",font=f1,pady=10)
snake.grid(column=0,row=4)
snake.bind("<Button-1>",snake_fn)

label3=Label(app,text="")
label3.grid(column=0,row=5)

tetris=Button(app,text="Tetris",font=f1,pady=10)
tetris.grid(column=0,row=6)
tetris.bind("<Button-1>",tetris_fn)

label4=Label(app,text="")
label4.grid(column=0,row=7)

maze=Button(app,text="Maze",font=f1,pady=10)
maze.grid(column=0,row=8)
maze.bind("<Button-1>",maze_fn)

label5=Label(app,text="")
label5.grid(column=0,row=9)

pong=Button(app,text="Pong",font=f1,pady=10)
pong.grid(column=0,row=10)
pong.bind("<Button-1>",pong_fn)

label6=Label(app,text="")
label6.grid(column=0,row=11)

falling_skies=Button(app,text="Falling skies",font=f1,pady=10)
falling_skies.grid(column=0,row=12)
falling_skies.bind("<Button-1>",falling_skies_fn)

wn.mainloop()