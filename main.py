from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter import dialog
import os


win = Tk()
win.title('Digital White Board')
win.geometry('1050x570+150+50')
win.config(bg='#f2f3f5')
win.resizable(False, False)

image_icon = PhotoImage(file='logo.png')
win.iconphoto(False, image_icon)

color_box = PhotoImage(file='color section.png')
Label(win, image=color_box, bg='#f2f3f5').place(x=10, y=20)

eraser = PhotoImage(file='eraser.png')
Button(win, image=eraser, bg='#f2f3f5').place(x=30, y=400)

importimage = PhotoImage(file='addimage.png')
Button(win, image=importimage, bg='white').place(x=30, y=450)

colors = Canvas(win, bg='#fff', width=37, height=300, bd=0)
colors.place(x=30, y=60)

canvas = Canvas(win, width=930, height=500, background='white', cursor='hand2')
canvas.place(x=100, y=10)


win.mainloop()