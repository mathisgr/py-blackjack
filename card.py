class Card(object):

    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        
    def is_ace(self):
        return self.rank == 'A'
    
    def __str__(self):
        return self.suit + ':' + self.rank  