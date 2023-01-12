class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.guessed_letters = []
        self.hidden_phrase = ["_" if letter != " " else " " for letter in phrase]
        
    def show_phrase(self, letter):
        if letter != " ":
            self.guessed_letters.append(letter)
        for i, char in enumerate(self.phrase):
            if char == letter:
                self.hidden_phrase[i] = letter

    def check_win(self):
        return "_" not in self.hidden_phrase

    def display(self):
        phrase_display = []
        for i, char in enumerate(self.phrase):
            if char in self.guessed_letters:
                phrase_display.append(char)
            else:
                phrase_display.append("_")
            if char == " ":
                phrase_display.append(" ")
        print(" ".join(phrase_display))

    