#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary
from src.pick_word import pick_word
import src.config as config
from src.rect_word import *

def check_entry(entry, window, canvas):
    """
    Check user input
    """
    sel = entry.get().lower() 
    
    # check user input is only 5 letters
    if not sel.isalpha():
        messagebox.showerror("Only letters", "You entered numbers and/or special characters!")
        entry.delete(0, END)
        return 
    elif len(sel) > 5:
        messagebox.showerror("Must be 5 letter", "You entered more than 5 letters!")
        entry.delete(0, END)
        return 
    elif len(sel) < 5:
        messagebox.showerror("Must be 5 letter", "You entered less than 5 letters!")
        entry.delete(0, END)
        return 
    
    # check if word exist
    dict = PyDictionary
    if dict.meaning(sel) == None and sel != config.chosen_word:
        messagebox.showerror("Word doesn't exists", "You entered a word that does not exist!")
        entry.delete(0, END)
        return
    
    
    # word is correct
    if sel == config.chosen_word:
        # return user input
        tries(window=window, canvas=canvas, input=sel)
        
        # winning stats
        percent_win_one_game = ((6-config.click_count)/6) * 100
        config.avg_win_percent += percent_win_one_game
        config.winning_streak += 1
        config.distribution[str(config.click_count+1)] += 1
        
        messagebox.showinfo("Word is correct", "Congrats you guessed the word!\nGuess(es): {}, Game(s): {}\n% Win:{:.2f}%, Avg % Win: {:.2f}%\n Winning Streak: {} tries\nDistribution: {}"
                            .format(config.click_count+1, config.game_count, 
                                    percent_win_one_game, (config.avg_win_percent/config.game_count),
                                    config.winning_streak, config.distribution))    

        return window.destroy()
    
    else:
        # wrong word
        entry.delete(0, END)
        tries(window=window, canvas=canvas, input=sel)
        
        # run out of tries
        if config.click_count == 5:
            messagebox.showerror("No more tries", "You are out of tries!\n Correct word is: {}".format(config.chosen_word))
            return window.destroy()
        return
    
    
