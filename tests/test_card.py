'''Test module for Card module'''
import unittest
from app.card import Card

class TestCard(unittest.TestCase):
    '''Test class for Card module'''

    def test_one(self):
        '''Check the testcard string repsentation'''
        testcard = Card('Hearts', 'King')
        self.assertEqual(str(testcard), 'King of Hearts')

if __name__ == "__main__":
    unittest.main()
