import os

clear = lambda: os.system('clear')

class Display:

    def __init__(self, hangman) -> None:
        self.HANGMAN = hangman
        self.player = hangman.player
        self.word = hangman.word

            
    def __str__ (self) -> str:
        clear()
        return f""" 
                {self.HANGMAN.show()} 
                {self.word.show_hidden()} 
                {self.player}"""

