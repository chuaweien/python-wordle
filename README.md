# Python-wordle

Attempt to recreate wordle in Python using `Tkinter` module.

## File structure

- `dictionary`
  - `words.txt` - used to generate the word
- `src`
  - `check.py` - check whether the entry is valid and whether the guess is correct
  - `config.py` - set global variables
  - `create_window.py` - create GUI window
  - `pick_word.py` - pick a word from `words.txt`
  - `rect_word.py` - replace rectangles into input letters in GUI
- `requirements.txt` - packages to install

## Steps to run

1. Start venv
2. Install `requirements.txt`
3. Run `main.py`

## How it works

A game starts and the user has 6 guesses for a word before his tries run out. Only 5-letter words which are valid in `PyDictionary` are accepted.

After a win, a pop up window will show the number of guesses took and the winning statistics.

The color of the letters mean:

- Green: Right letter in the right position
- Orange: Right letter in the wrong position
- Red: Wrong letter

After 6 wrong guesses, the correct word will be shown and the next game starts. 

To end the game, press `Ctl + C` in the terminal.

## References

<https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt>
