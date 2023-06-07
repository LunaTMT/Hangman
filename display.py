import os
import sys
from hangman import Hangman
clear = lambda: os.system('clear')

class Display:

    def __init__(self, player, word) -> None:
        self.p = player
        self.w = word
        self.HANGMAN = Hangman()
        
            
    def __str__ (self):
        clear()
        print("\t\t", self.HANGMAN.show(self.p.lives))
        print()
        print("\t\t", self.w.fill_guesses(self.p.guess))
        print("\t\t", self.p)
        print()

        if self.p.lives == 0:
            self.end_game("L")
        elif self.p.correct == self.w.length:
            self.end_game("W")
        else:
            return ""
    
    
    def end_game(self, state):
        clear()
        print("\t\t", self.HANGMAN.show(self.p.lives))
        print()
        print("\t\t", self.w)
        print("\t\t", self.p)
        
        
        

        match state:
            case "W":
                print("\t\t You Win!")
            case "L":
                print("\t\t Unlucky Chump :(")
            case "_":
                pass
        sys.exit()
            
