from deck import Deck
from dealer import Dealer
from player import Player
from blackjackhand import BlackjackHand
 

class GameController(object):
    
    def __init__(self):
        self.player_bet = 0
        
    def prep_player(self):
        self.player = Player()
    
    def prep_dealer(self):
        deck = Deck()
        deck.shuffle()
        self.dealer = Dealer(deck)
    
    def ask_player_bet(self):
        self.player_bet = self.player.ask_bet()
    
    def hand_to_player(self):
        self.player.take_card(self.dealer.deal_card()) 
        self.player.take_card(self.dealer.deal_card())
        self.player.show_hand()
        
    def hand_to_dealer(self):
        self.dealer.take_card(self.dealer.deal_card()) 
        self.dealer.take_card(self.dealer.deal_card())
        self.dealer.show_hand()
        
    def check_initial_hands(self):
        if self.dealer.hand.is_blackjack() and self.player.hand.is_blackjack():
            print 'Both you and the dealer have Blackjack!'
            self.dealer.show_hand(False)
            return 'tie'
             
        if self.dealer.hand.is_blackjack():
            print 'Dealer has Blackjack!'
            self.dealer.show_hand(False)
            return 'dealer'
            
        if self.player.hand.is_blackjack():
            print 'Player has Blackjack'
            return 'player'
            
        return 'game goes on'
        
    def process_blackjack(self, outcome):
        if outcome == 'player':
            self.player.add_win(1.5 * self.player_bet)
            return
        
        if outcome == 'dealer':
            self.player.sub_loss(self.player_bet)
            return
        
    def do_player_turn(self):
        
        while self.player.hand.is_busted() == False:
            answer = self.player.play_turn()
            
            if answer == 'h':
                self.player.take_card(self.dealer.deal_card())
                self.player.show_hand()
                continue 
                
            if answer == 's':
                return
            
    def do_dealer_turn(self):
        self.dealer.play_turn() 
        
    def check_player(self):
        if self.player.hand.is_busted() == True:
            print "You are busted!"
            return 'player_busted'
        else:
            return 'player_ok'
            
            
    def check_dealer(self):
        if self.dealer.hand.is_busted() == True:
            print "Dealer is busted!"
            return 'dealer_busted'
        else:
            return 'dealer_ok'

    def find_winner(self):

        if self.dealer.hand.get_total() == self.player.hand.get_total():
            print 'Both you and the dealer have: ' + str(self.player.hand.get_total())
            self.dealer.show_hand(False)
            return 'tie'
             
        elif self.dealer.hand.get_total() < self.player.hand.get_total():
            print 'You win with: ' + str(self.player.hand.get_total())
            return 'player'
            
        else:
            print 'Dealer wins with: ' + str(self.dealer.hand.get_total())
            return 'dealer'
            
    def handle_game_outcome(self, outcome):
        
        if outcome == 'player':
            self.player.add_win(self.player_bet)
            
        elif outcome == 'dealer':
            self.player.sub_loss(self.player_bet)
            
        else:
            return
        
    def collect_used_cards(self):
        self.player.hand = BlackjackHand()
        self.dealer.hand = BlackjackHand()
        
    def ask_play(self):
        while True:
            answer = raw_input('Do you want to play Blackjack? [yn]')
            if answer in 'ynYN':
                return answer.lower() == 'y'