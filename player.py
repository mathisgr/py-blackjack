from blackjackhand import BlackjackHand

class Player(object):
    
    def __init__(self, bankroll = 100):
        self.bankroll = bankroll
        self.hand = BlackjackHand()
        
    def add_win(self, amount):
        self.bankroll += amount
        print 'You win ' + str(amount) + '$. You now have ' + str(self.bankroll) + '$'
        
    def sub_loss(self, amount):
        self.bankroll -= amount
        print 'You lose ' + str(amount) + '$. You now have ' + str(self.bankroll) + '$'
        
    def take_card(self, card):
        self.hand.add_card(card)
        
    def empty_hand(self):
        self.hand = BlackjackHand()
        
    def show_hand(self):
        self.hand.show(False)
        
    def ask_bet(self):
        bet = 0
        while True:
            try: 
                bet = int(raw_input('What is your bet?'))
            except:
                print 'Please enter a positive number.'
                continue 
                
            if bet <= 0:
                print 'Please enter a positive number.'
                continue
                
            if bet > self.bankroll:
                print "You don't have enough money for this bet."
                continue
                
            if bet == self.bankroll:
                print 'Betting the farm!'
                
            return bet 
        
    def play_turn(self):
        while True:
            answer = raw_input('Do you want to [h]it or [s]tay? ')
            if answer in 'hsHS':
                return answer.lower()