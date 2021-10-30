import random

from ProjectPython.DeckOfCards import DeckOfCards
from ProjectPython.Player import Player
from ProjectPython.Card import Card
class CardGame:
    def __init__(self,name1,name2,numbers_cards_for_player=26):
        self.player1=Player(name1,numbers_cards_for_player)
        self.player2=Player(name2,numbers_cards_for_player)
        self.pack_of_cards=DeckOfCards()
    def new_game(self):
        self.pack_of_cards.cards_shuffle()
        self.player1.set_hand(self.pack_of_cards)
        self.player2.set_hand(self.pack_of_cards)
    #     # if len(self.pack_of_cards) < 52:
    #     #     print("Error")
    # def new_game(self):

        # self.player1_cards=Player.set_hand(self.pack_of_cards)
        # self.player2_cards=Player.set_hand(self.pack_of_cards)
    def get_winner(self):
        # if self.player1.numbers_cards_for_player > self.player2.numbers_cards_for_player:
        #     return f"{self.player1} is winner"
        # elif  self.player1.numbers_cards_for_player < self.player2.numbers_cards_for_player:
        #     return f"{self.player2} is winner"
        # elif self.player1.numbers_cards_for_player == self.player2.numbers_cards_for_player:
        #     return None
        if len(self.player1.cards_of_player) > len(self.player2.cards_of_player):
            return f"Win the Player1"
        elif len(self.player1.cards_of_player) < len(self.player2.cards_of_player):
            return f"Win the Player2"
        else:
            return None
    def __repr__(self):
        return f"{self.player1},{self.player2},{self.pack_of_cards}"
    # def __str__(self):
    #     return f"{self.new_game()}"

# Game1=CardGame("michael","lidor",26)
# Game1.new_game()
# print(Game1.player1)
# print(Game1.player2)
# for i in range(1):
#     print(Game1.player1.get_card())
#     print(Game1.player2.get_card())
#     if Game1.player1.get_card()>Game1.player2.get_card():
#         Game1.player1.add_card(Game1.player1.get_card())  and   Game1.player1.add_card(Game1.player2.get_card())
#
#     else:Game1.player2.add_card(Game1.player1.get_card()) and Game1.player2.add_card(Game1.player2.get_card())
#     print(len(Game1.player1.cards_of_player))
#     print(len(Game1.player2.cards_of_player))
#     print(Game1.player1)
#     print(Game1.player2)
#     print(Game1.get_winner())





