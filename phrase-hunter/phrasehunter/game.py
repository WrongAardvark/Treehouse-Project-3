import random

class Game:
    #this is the game class to contain call my game attributes
    def __init__(self):
        self.missed = 0
        self.phrases = ["The power of the dark side", "I am your father", "May the Force be with you", "This is the way", "I have a bad feeling about this"]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = []

        def display(self, guesses):

            for letter in self.phrase:
                if letter in self.phrase:
                    print(f"{letter}", end=" ")
                else:
                    print("_", end=" ")
    
        

        
