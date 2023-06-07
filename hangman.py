class Hangman:

    def __init__(self) -> None:
        self.figure = [
            '________',
            '|       |',
            '|       O',
            '|       |',
            '|      /|\ ',
            '|       |',
            '|      / \ ']
    
    def show(self, lives) -> str:
        HM_pic = '\n\t\t'.join(self.figure[:7 - lives])
        return HM_pic if lives < 7 else ''