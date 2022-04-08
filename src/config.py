#!/usr/bin/env python3

from src.pick_word import pick_word

# how many times you click on "Confirm"
click_count = -1

# chosen word
chosen_word = ""

# rectangles in GUI
rect = {}

# how many games
game_count = 0

# average percentage win
avg_win_percent =  0

# winning streak 
winning_streak = 0

# winning distribution
distribution = {'1':0,
                '2':0,
                '3':0,
                '4':0,
                '5':0,
                '6':0}

# Letters used
letters = {}

used_letters = ""

alpha_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"