from random_word import RandomWords 

class Word:

    def __init__(self) -> None:
        self.w = "Cat".upper() #RandomWords().get_random_word().upper() 
        self.length = len(self.w)
        self._dict = dict.fromkeys(self.w, '_')
        self.guessed = 0

    def __str__(self):
        print(f"Word : {' '.join(self.w)}")
        return ""

    def fill_guesses(self, guess):
        if guess in self._dict:
            self._dict[guess] = guess            
        return " ".join(self._dict[c] for c in self.w)
    