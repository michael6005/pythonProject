from ProjectPython.DeckOfCards import DeckOfCards
from ProjectPython.Player import Player
from ProjectPython.Card import Card
from ProjectPython.CardGame import CardGame
Game1=CardGame("michael","lidor",26)
Game1.new_game()
print(Game1.player1)
print(Game1.player2)
for i in range(1):
    card_player1=Game1.player1.get_card()
    card_player2=Game1.player2.get_card()
    print(card_player1)
    print(card_player2)
    if card_player1>card_player2:
        Game1.player1.add_card(card_player1)  and   Game1.player1.add_card(card_player2)

    else: Game1.player2.add_card(card_player1) and Game1.player2.add_card(card_player2)
    print(len(Game1.player1.cards_of_player))
    print(len(Game1.player2.cards_of_player))
    print(Game1.player1)
    print(Game1.player2)
    print(Game1.get_winner())