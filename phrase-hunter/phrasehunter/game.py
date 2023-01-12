# Create your Game class logic in here.
import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("hello world"), Phrase("python is fun"), Phrase("object oriented programming"), Phrase("let's play"), Phrase("This is a test")]
        self.active_phrase = None
        self.guesses = []
        
    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        while not self.active_phrase.check_win() and self.missed < 5:
            self.active_phrase.display()
            guess = self.get_guess()
            if guess in self.active_phrase.phrase:
                self.active_phrase.show_phrase(guess)
            else:
                self.missed += 1
                print(f"Incorrect. Number of attempts remaining: {5 - self.missed}.")
            if self.active_phrase.check_win():
                self.game_over("win")
        if self.missed == 5:
            self.game_over("lose")
            
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("Welcome to the Phrase Hunter Game!!!!!!!")
        print("Guess the phrase by entering one letter at a time.")
        print("You have 5 incorrect guesses before the game is over.")
        
    def get_guess(self):
        guess = input("Guess a letter: ")
        self.guesses.append(guess)
        return guess
        
    def game_over(self, outcome):
        if outcome == "win":
            print("Congratulations! You win.")
            print(f"The phrase was {self.active_phrase.phrase}")
        else:
            print("Sorry, you lose.")
            print(f"The phrase was {self.active_phrase.phrase}")
