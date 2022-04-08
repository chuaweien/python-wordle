#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox, ttk

from src.check import check_entry
import src.config as config
from src.pick_word import pick_word

def create_window():
    # intialising window
    window = Tk()
    window.title("Python - Guess the five-letters word")
    window_width = 500
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coor = int((screen_width - window_width)/2)
    y_coor = int((screen_height - window_height)/2)
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coor, y_coor))

    # setting words on window
    greeting = Label(text="Hello Player! \n Welcome to Python Guess the five-letter word \n Please enter 5 letters.")
    greeting.pack()

    # user input
    entry = Entry(window)
    entry.pack(pady = 10)
    

    # button for confirm selection
    cfm_button = Button(window, text="Confirm", command = lambda: check_entry(entry=entry, 
                                                                          window=window, 
                                                                          canvas=canvas,)).pack(padx = 10, pady = 10)
    
    # create rectangles
    x1 = 150
    y1 = 50
    canvas = Canvas(window, width=500, height=500)
    canvas.pack()
    for j in range(0,6):
        for i in range(0,5):
            config.rect["rect{}{}".format(i,j)] = canvas.create_rectangle((i*40)+x1, (j*40)+y1, (i*40)+(x1+30), (j*40)+(y1+30), fill='gray')

    config.letters["used"] = canvas.create_text((250,10), text = "Used Letters: {}".format(config.used_letters), fill="gray")
    config.letters["unused"] = canvas.create_text((250,30), text = "Unused Letters: {}".format(config.alpha_list), fill="blue")
    
        
    window.mainloop()
    
    