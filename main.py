#!/usr/bin/env python3

import src.config as config
from src.create_window import create_window
from src.pick_word import pick_word
from collections import OrderedDict


def main():
    config.chosen_word = pick_word()
    config.click_count = -1
    config.game_count += 1
    config.used_letters = ""
    create_window()
    main()

if __name__ == '__main__':
    main()

