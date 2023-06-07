from player import Player
from display import Display
from word import Word


class HangmanInterface:
    
    def run():
        w = Word()
        p = Player(w)
        d = Display(p, w)
        while p.lives >= 0:
            print(d)
            p.get_guess()
        
        
