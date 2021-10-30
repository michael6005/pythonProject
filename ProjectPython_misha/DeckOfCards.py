from ProjectPython.Card import Card
import random
from random import randint
from random import shuffle
class DeckOfCards:
    def __init__(self):
        self.deck_cards=[]
        for suit in range(1, 5):
            for value in range(1,14):
                self.deck_cards.append(Card(value,suit))
    def cards_shuffle(self):
        random.shuffle(self.deck_cards)
    def deal_one(self):
        card=random.choice(self.deck_cards)
        self.deck_cards.remove(card)
        return card
    def __repr__(self):
        return f"{self.deck_cards}"

# Deck1=DeckOfCards()
# print(Deck1)
# Deck1.cards_shuffle()
# print(Deck1.deal_one())
# print(Deck1)