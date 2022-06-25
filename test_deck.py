import unittest
from deckofcards import Deck, Card

class TestCard(unittest.TestCase):

	def setUp(self):
		self.card = Card("Hearts", "A")


	def test_init(self):
		self.assertEqual(self.card.value, 'A')
		self.assertEqual(self.card.suit, 'Hearts')

	def test_repr(self):
		self.assertEqual(self.__repr__(), "A of Hearts")

class TestDeck(unittest.TestCase):

	def setUp(self):
		self.deck = Deck()

	def Deck_init(self):
		self.assertEqual(len(self.deck.cards), 52)
		self.assertTrue(isinstance(self.deck.cards, list))

	def test_repr(self):
		self.assertEqual(__repr__(self.deck), "Deck of 52 cards")

	def test_count(self):
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

if __name__ == "__main__":
	unittest.main()