
class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase
        

    def display(self, guesses):

        for letter in self.phrase:
            if letter in self.phrase:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
