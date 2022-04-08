#!/usr/bin/env python3

import random
from tkinter import messagebox

filepath = "./dictionary/words.txt"

def pick_word():
    """
    Pick word from dictionary and compare to user input. 
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()
        lines = [line.strip("\n") for line in lines]
        index = random.randint(0, 5756)
    
    chosen_word = lines[index]
    
    return chosen_word