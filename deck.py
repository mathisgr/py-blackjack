import random
from card import Card

class Deck(object):
    
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['C','D','H','S']


    def __init__(self):
        self.deck = []
        for s in Deck.suits:
            for r in Deck.ranks:
                self.deck.append(Card(s,r))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

    def show(self):
        for card in self.deck:
            print card