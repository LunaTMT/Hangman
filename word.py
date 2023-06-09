from random_word import RandomWords 

class Word(dict):

    def __init__(self) -> None:
        self.word = "Cat".upper() #RandomWords().get_random_word().upper() 
        self.length = len(self.word)
        super().__init__(dict.fromkeys(self.word, '_'))

    def __str__(self) -> str:
        return f" Word : {self.word}"

    def show_hidden(self) -> str:
        return f" Word : {' '.join(self[c] for c in self.word)}"

