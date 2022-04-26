
class Phrase:
    
    def __init__(self, phrase):
        self.phrase_list = ["The power of the dark side", 
                            "I am your father", 
                            "May the Force be with you", 
                            "This is the way", 
                            "I have a bad feeling about this"]

    def display(self, guesses):

        for letter in self.phrase:
            if letter in self.phrase:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
