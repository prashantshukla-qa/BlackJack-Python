'''Test module for Deck Module'''
import unittest
from app.deck import Deck
from app.card import Card, SUITES, RANKS

class TestDeck(unittest.TestCase):
    '''Using unittest module ffor testing deck class'''

    def test_two(self):
        '''Testing for the length of the Deck object'''
        testdeck = Deck(SUITES, RANKS)
        self.assertEqual(len(testdeck.deck), 52)

    def test_three(self):
        '''Testing for the first card of the deck'''
        testdeck = Deck(SUITES, RANKS)
        self.assertEqual(testdeck.deck[0], Card(SUITES[0], RANKS[0]))
        