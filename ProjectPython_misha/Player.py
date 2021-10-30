from ProjectPython.Card import Card
from ProjectPython.DeckOfCards import DeckOfCards
import random

class Player:
    def __init__(self,name,numbers_cards_for_player=26):
        self.name=name
        self.numbers_cards_for_player=numbers_cards_for_player
        self.cards_of_player=[]
    def __str__(self):
        return f"{self.name}:,{self.cards_of_player}"
    def set_hand(self,deck_of_cards:DeckOfCards):
       for i in range(self.numbers_cards_for_player):
            self.cards_of_player.append(deck_of_cards.deal_one())
    def get_card(self):
        random_card=random.choice(self.cards_of_player)
        return random_card
    def add_card(self,card):
        self.cards_of_player.append(card)

    def __repr__(self):
        return f"{self.name}:,{self.cards_of_player}"


#if __name__=="__main":
# Player1 = Player("michael", 10)
# Player2 = Player("lidor", 10)
# Deck1 = DeckOfCards()
# Player1.set_hand(Deck1)
# Player2.set_hand(Deck1)
# print(Player1)
# x = Player1.get_card()
# print(x)
# Player2.add_card(x)
# print(Player1)
# print(Player2)



