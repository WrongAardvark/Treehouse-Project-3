class Game:
    #this is the game class to contain call my game attributes
    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = [""]

    def create_phrases(self):
        self.phrases = self.phrases.append("The power of the dark side", "I am your father", "May the Force be with you", "This is the way", "I have a bad feeling about this")
        return self.phrases

        
