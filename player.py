from collections import defaultdict

class Player(dict):

    def __init__(self) -> None:
        self.guess = ""
        self.lives = 7
        self.correct = 0

    
    def __str__(self) -> str:
        guesses = (key for key in sorted(self.keys()))
        return f"""
                 Guesses : {' '.join(guesses) if guesses else 'Guesses: None' }
                 Lives   : {self.lives}"""

    
    def get_guess(self) -> None:
        
        guess = input("\t\t Guess   : ")
        while True:
            if not guess.isalpha():
                guess = input("\nPlease enter a letter : ")
            elif len(guess) > 1:
                guess = input("\nPlease only enter a single letter : ")
            elif guess.upper() in self:
                guess = input(f"\nYou have already chosen '{guess.upper()},' Please enter a new guess : ")
            else: break
            
        guess = guess.upper()
        self[guess] = 1
        self.guess = guess
        
