from player import Player
from display import Display
from word import Word
from hangman import Hangman

class HangmanInterface:
    
    def __init__(self) -> None:
        self.player  =  Player()
        self.word    =    Word()
        self.hangman = Hangman(self.player, self.word)
        self.display = Display(self.hangman)
        
    def run(self) -> None:
        while self.player.lives >= 0:
            print(self.display)
            self.player.get_guess()
            self.hangman.verify()
            

        
        
