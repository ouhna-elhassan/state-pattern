from tkinter import * 
import tkinter as tk
from states import *
from controller import Context

#main programm
fenetre = Tk()
fenetre.title('Design patterns: State')

label = Label(fenetre, text="State-pattern")
label.grid(row = 0, column = 0,)

#initilize state of context
red = RedState()
context = Context(red)
color = context.get_state().getColor()

#functions
def pushButton():
    context.push()
    global canvas
    color = context.state.getColor()
    print(color)
    canvas.configure(bg=color)

def pullButton():
    context.pull()
    global canvas
    color = context.state.getColor()
    canvas.configure(bg=color)

#create canvas interface
canvas = Canvas(fenetre, 
                width=300,
                height=300,
                bd=50,
                highlightthickness=5,
                highlightbackground="yellow",
                background =context.get_state().getColor()
        )
canvas.grid(row = 1, column = 0,columnspan = 5, padx = 3, pady = 3)

#buttons
bouton=Button(fenetre, text="Push",width= 25, height= 3,  command=lambda: pushButton())
bouton.grid(row = 6, column = 0, padx = 3, pady = 3, sticky=E)

bouton=Button(fenetre, text="Pull",width= 25, height= 3, command=lambda: pullButton())
bouton.grid(row = 6, column = 1, padx = 3, pady = 3, sticky=E)

bouton=Button(fenetre, text="Exit",width= 25, height= 3, command=fenetre.quit)
bouton.grid(row = 6, column = 2, padx = 3, pady = 3, sticky=E)

fenetre.mainloop()