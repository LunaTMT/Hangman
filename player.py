from collections import defaultdict

class Player:

    def __init__(self, word) -> None:
        self.guesses = defaultdict(lambda: True) #
        self.guess = ""
        self.lives = 7
        self.correct = 0
        self.word = word
    
    def __str__(self):

        guesses = (key for key in sorted(self.guesses.keys()))
        return f"""
                Guesses: '{' '.join(guesses) if guesses else 'Guesses: None' }
                Lives: {self.lives}"""
        
    
    def get_guess(self):
        
        guess = input("Please enter your guess :")
        while True:
            if not guess.isalpha():
                guess = input("Please enter a letter :")
            elif len(guess) > 1:
                guess = input("Please only enter a single letter :")
            elif guess.upper() in self.guesses:
                guess = input(f"You have already chosen '{guess.upper()},' Please enter a new guess :")
            else: break
            
        guess = guess.upper()
        self.guesses[guess] += 1
        
        if guess not in self.word._dict:
            self.lives -= 1
        else:
            self.correct += 1

        self.guess = guess
        
