class Card(object):
    """
    This class describes the Card object. Holds a Card's suit and value. 
    Card's value ranges from 2 to 14, with 2-10 being the standard numerical 
    representations. And 11-14 being the face Cards (Jack, Queen, King, Ace).
    """
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.val = value

    def show(self) -> None:
        """
        Getter method to display card suit and value, also converts values above 
        10 to appropriate Face card name (i.e. Jack, Queen, King, Ace)
        """
        if self.val == 11:
            card_val = "Jack"
        elif self.val == 12:
            card_val = "Queen"
        elif self.val == 13:
            card_val = "King"
        elif self.val == 14:
            card_val = "Ace"    
        else:
            card_val = self.val
        print("{} of {}".format(card_val, self.suit))


# Testing Driver code

# card = Card("Hearts", 12) # queen of hearts
# card.show()
