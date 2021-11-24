from Card import Card
from Deck import Deck
from typing import Union


class Player(object):
    """
    Each Player has a "name" and "hand" attribute associated with them. This class allows modification of a Player's hand, which holds a number of cards. It also has some getter methods to display information about the player.
    """
    def __init__(self, name:str, hand:list = []) -> None:
        self.name = name
        self.hand = hand # list of cards fed in, defaults to empty hand

    def displayHand(self) -> None:
        print("Player {}'s hand: ".format(self.name))
        for card in self.hand:
            if card:
                print(card.show())

    def handCount(self) -> int:
        # returns number of cards in the Player's hand
        return len(self.hand)

    def collectCards(self, cards:list) -> None:
        """
        Takes list of Cards to be collected and adds it to the end of the Player's hand.
        Small assumption: since order of cards being added to hand is fixed, it's in spirit of War game mechanics.
        the first card added to the end of the hand is the "first" card to have been played in the list/pile.
        """
        self.hand = self.hand + cards
    
    def playCard(self) -> Union[Card, bool]:
        """
        Plays the Card from the front of the Player's hand. Returns False if no Card left in Player's hand
        """
        card = self.hand.pop(0) if self.hand else False
        return card
    

