#!/usr/bin/env python3

from hashlib import new
from tkinter import *
from tkinter import messagebox
from collections import OrderedDict
import src.config as config

def tries(window, canvas, input):
    """Replacing rectangles with letters"""
    # valid try
    config.click_count += 1
    
    # delete previous letter lists
    canvas.delete(config.letters["used"])
    canvas.delete(config.letters["unused"])

    config.used_letters += input.upper()
    config.used_letters = " ".join(sorted(OrderedDict.fromkeys(config.used_letters)))
    
    config.unused_letters = alpha_colours()
    
    # add letter lists
    config.letters ["used"]= canvas.create_text((250,10), text = "Used Letters: {}".format(config.used_letters), fill="gray")
    config.letters ["unused"] = canvas.create_text((250,30), text = "Unused Letters: {}".format(config.unused_letters), fill="blue")
    
    # Label(text="Chosen word is {}".format(config.chosen_word)).place(x =100, y=170) # show the chosen word
    
    
    for i in range(0,5):
        # double letter counts
        double_letter = 0
        if input.count(input[i]) > config.chosen_word.count(input[i]):
            double_letter = 1
        # replace rectangle with letters
        canvas.delete(config.rect["rect{}{}".format(i,config.click_count)])
        letters = Label(text=input[i].upper(), fg=colours(input[i], i, double_letter), font=15).place(x=160+(i*40), y=190+(config.click_count*40))
        
    

        
        
def colours(input, index, double_letter):
    """
    Colors for letters depeneding on below conditions:
        green - correct letter at correct position
        orange - correct letter at wrong position
        red - wrong letter
    """
    if input == config.chosen_word[index]:
        return "green"
    if input in config.chosen_word and double_letter == 0:
        return "orange"
    else:
        return "red"
    
def alpha_colours():
    """new list of unused letters"""
    new_list = ""
    for x in config.alpha_list:
        if x not in config.used_letters:
            new_list += "{} ".format(x)
    return new_list

