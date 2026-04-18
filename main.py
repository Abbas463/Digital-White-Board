import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter import filedialog
import os


win = Tk()
win.title('Digital White Board')
win.geometry('1050x570+150+50')
win.config(bg='#f2f3f5')
win.resizable(False, False)

current_x = 0
current_y = 0
color = 'black'
line_width = 1
selected_image = None
image_start_x = 0
image_start_y = 0
dragging_image = False

def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y

def addline(work):
    global current_x, current_y, line_width
    canvas.create_line((current_x, current_y, work.x, work.y),
                       fill=color, width=line_width, capstyle=ROUND, smooth=TRUE)
    current_x, current_y = work.x, work.y


def show_color(new_color):
    global color
    color = new_color
    canvas.config(cursor='hand2')

def select_color(event, new_color):
    global color
    color = new_color
    canvas.unbind('<Button-1>')
    canvas.unbind('<B1-Motion>')
    canvas.bind('<Button-1>', locate_xy)
    canvas.bind('<B1-Motion>', addline)

def new_canvas():
    canvas.delete('all')
    display_pallete()

def insertimage():
    global filename, f_image, selected_image
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select image file',
    filetypes=(('PNG file', '*.png'), ('All files', '*.*')))
    f_image = PhotoImage(file=filename)
    selected_image = canvas.create_image(180, 50, image=f_image)
    canvas.tag_bind(selected_image, '<Button-1>', start_drag)
    canvas.tag_bind(selected_image, '<B1-Motion>', drag_image)
    canvas.tag_bind(selected_image, '<ButtonRelease-1>', stop_drag)
    # Disable drawing functionality until a color is selected
    canvas.unbind('<Button-1>')
    canvas.unbind('<B1-Motion>')

def start_drag(event):
    global selected_image, image_start_x, image_start_y, dragging_image
    dragging_image = True
    image_start_x = event.x
    image_start_y = event.y

def drag_image(event):
    global selected_image, image_start_x, image_start_y, dragging_image
    if dragging_image and selected_image:
        dx = event.x - image_start_x
        dy = event.y - image_start_y
        canvas.move(selected_image, dx, dy)
        image_start_x = event.x
        image_start_y = event.y

def stop_drag(event):
    global dragging_image
    dragging_image = False

image_icon = PhotoImage(file='logo.png')
win.iconphoto(False, image_icon)

color_box = PhotoImage(file='color section.png')
Label(win, image=color_box, bg='#f2f3f5').place(x=10, y=20)

eraser = PhotoImage(file='eraser.png')
Button(win, image=eraser, bg='#f2f3f5', command=new_canvas).place(x=30, y=400)

importimage = PhotoImage(file='addimage.png')
Button(win, image=importimage, bg='white', command=insertimage).place(x=30, y=450)

colors = Canvas(win, bg='#fff', width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill='black')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'black'))

    id = colors.create_rectangle((10, 40, 30, 60), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'gray'))

    id = colors.create_rectangle((10, 70, 30, 90), fill='brown4')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'brown4'))

    id = colors.create_rectangle((10, 100, 30, 120), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'red'))

    id = colors.create_rectangle((10, 130, 30, 150), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'orange'))

    id = colors.create_rectangle((10, 160, 30, 180), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'yellow'))

    id = colors.create_rectangle((10, 190, 30, 210), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'green'))

    id = colors.create_rectangle((10, 220, 30, 240), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'blue'))

    id = colors.create_rectangle((10, 250, 30, 270), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: select_color(x, 'purple'))

display_pallete()

canvas = Canvas(win, width=930, height=500, background='white', cursor='hand2')
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addline)


current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    global line_width
    line_width = current_value.get()
    value_label.configure(text=get_current_value())

slider = ttk.Scale(win, from_=1, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(win, text=get_current_value())
value_label.place(x=27, y=550)

win.mainloop()