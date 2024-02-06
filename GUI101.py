"""
The aim of this document is to provide a easy understanding of the library tkinter

on terminal:
pip install tk

Deeper understanding:
https://www.youtube.com/watch?v=YXPyB4XeYLA

Documentations
https://www.geeksforgeeks.org/python-gui-tkinter/
https://www.pythontutorial.net/tkinter/
"""

import tkinter as tk
from tkinter import *


def action101(event=None):
    user_login = login_box.get()
    user_pwd = pin_box.get()
    return print("Hello user {} your pwd is {}".format(user_login, user_pwd))


if __name__ == '__main__':
    '''Font & Colors'''
    # rgb
    orange_rgb = (255, 153, 0)
    blue_rgb = (35, 47, 62)
    white_font = (255, 255, 255)

    # hexadecimal
    blue_hex = "#232F3E"
    orange_hex = '#FF9900'
    green_hex = "#00464F"
    white_hex = "#FFFFFF"

    '''GUI Interface'''
    # Size of the window app
    HEIGHT = 500
    WIDTH = 600

    '''Canvas'''
    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=blue_hex)
    canvas.pack()
    # canvas.pack(fill=X, padx=5, pady=5)

    '''Frame'''
    frame = tk.Frame(root, width=500, height=400, bg=white_hex, bd=5)
    frame.place(x=50, y=50)

    '''Labels'''
    label_mx = tk.Label(frame, text='GUI_101', bg=orange_hex)
    label_mx.config(font=('amazon_ember', 20))
    label_mx.config(fg=white_hex)
    label_mx.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    '''Login'''
    login_box = tk.Entry(frame, width=40)
    login_box.place(x=145, y=180)
    login_label = tk.Label(frame, text='LOGIN', bg=green_hex)
    login_label.config(font=('amazon_ember', 10))
    login_label.config(fg=orange_hex)
    login_label.place(x=210, y=220)

    '''PWD'''
    pin_box = tk.Entry(frame, width=40, show='*')
    pin_box.place(x=185, y=260)
    pin_label = tk.Label(frame, text='PASSWORD', bg=green_hex)
    pin_label.config(font=('amazon_ember', 10))
    pin_label.config(fg=white_hex)
    pin_label.place(x=340, y=300)

    '''Actions'''

    ofa_button = Button(frame, text="Action101", width=20, command=action101)
    ofa_button.config(font=('amazon_ember', 10))
    ofa_button.place(x=50, y=100)

    root.eval('tk::PlaceWindow . center')
    root.title("GUI_101")

    root.mainloop()
