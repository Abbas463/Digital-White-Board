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

def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill='black')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 40, 30, 60), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((10, 70, 30, 90), fill='brown4')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((10, 100, 30, 120), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 130, 30, 150), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 160, 30, 180), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10, 190, 30, 210), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10, 220, 30, 240), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10, 250, 30, 270), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

display_pallete()

canvas = Canvas(win, width=930, height=500, background='white', cursor='hand2')
canvas.place(x=100, y=10)

slider = ttk.Scale(win, from_=1, to=100, orient='horizontal')
slider.place(x=30, y=530)

win.mainloop()