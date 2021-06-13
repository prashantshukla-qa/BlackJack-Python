'''[summary]'''

import random
from card import Card

class Deck:
    '''Deck Class'''

    def __init__(self, suits, ranks):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        '''Genrate random seq of card in the deck i.e. shuflle the deck'''
        random.shuffle(self.deck)

    def deal(self):
        '''Distribute the card amongst palyers'''
        single_card = self.deck.pop()
        return single_card
