import random
from phrase import Phrase

class Game:
    #this is the game class to contain call my game attributes
    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.active_phrase = random.choice(self.phrases)
        self.guesses = []

    def get_phrase_list(self):
        for phrase in phrase.Phrase.phrase_list:
            self.phrases.append(phrase)
    
        

        
