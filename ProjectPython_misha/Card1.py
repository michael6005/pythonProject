class Card:
    def __init__(self,suit,value):
        self.value = value
        self.suit = suit
        self.suits_names = ['Club','Diamond','Heart','Spades']
        self.value_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s : %s' % (self.value_names[self.value], self.suits_names[self.suit])

    def __cmp__(self, other):
        # сравнение мастей
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # масти совпадают ... сравнение рангов if self.value > other.value: return 1
        if self.value > other.value:
            return 1
        if self.value < other.value:
            return -1
        # ранги совпадают ... ничья
        return 0

    # def __gt__(self, other):
    #     if self.value > other.value:
    #         return True
    #     elif self.value == other.value and self.suit > other.suit:
    #         return True
    #     else:
    #         return False
    # def __repr__(self):
    #     return f"{self.value},{self.suits[self.suit]}"
Card1 = Card(2, 11)
print(Card1)