import sys

class Hangman:

    def __init__(self, player, word) -> None:
        self.figure = [
            '________',
            '|       |',
            '|       O',
            '|       |',
            '|      /|\ ',
            '|       |',
            '|      / \ ']
        
        self.player = player
        self.word = word
        self.game_state = None

    
    def show(self) -> str:
        HM_pic = '\n\t\t'.join(self.figure[:7 - self.player.lives])
        return HM_pic if self.player.lives < 7 else ''
    
    def verify(self):
        if self.player.guess not in self.word:
            self.player.lives -= 1
        else:
            self.player.correct += 1
            self.word[self.player.guess] = self.player.guess 

        self.end_game()

    def end_game(self):
        if self.player.lives == 0:
            self.game_state = "L"
        elif self.player.correct == self.word.length:
            self.game_state = "W"
        else: return 

        print("\t\t", self.word)
        match self.game_state:
            case "W":
                print("\t\t You Win!")
            case "L":
                print("\t\t Unlucky Chump :(")
            case "_":
                pass
        sys.exit()
            