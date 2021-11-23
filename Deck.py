from Card import Card
from random import randint

class Deck(object):
    """

    """
    def __init__(self) -> None:
        self.card_list = []
        self.construct()
        self.shuffle()
    
    def construct(self) -> None:
        """
        Builds a standard deck with 52 cards. 4 Suits (Clubs, Hearts, Diamonds, Spades). There are four Cards for each Value, one of each Suit. 
        """
        for val in range(2,15):
            for suit in ["Clubs", "Hearts", "Diamonds", "Spades"]:
                # create the respective Card object and add it to the list
                self.card_list.append(Card(suit, val))
    
    def shuffle(self)

# driver code
deck = Deck()
for c in deck.card_list:
    c.show()