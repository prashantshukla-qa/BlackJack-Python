import unittest
from app.card import Card

class TestCard(unittest.TestCase):

    def test_one(self):
        testcard = Card('Hearts', 'King')
        self.assertEqual(str(testcard), 'King of Hearts')

if __name__ == "__main__":
    unittest.main()