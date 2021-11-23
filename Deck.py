from Card import Card
from random import randint

class Deck(object):
    """
    Deck creates a collection of Card objects. Forms a standard 52 card deck with 4 suits, and 14 values.
    Constructs and shuffles the deck, allows user to draw() a single Card, or half the Deck.
    """
    def __init__(self) -> None:
        self.card_list = []
        self.construct()
        self.shuffle()
    
    def construct(self) -> None:
        """
        Builds a standard deck with 52 cards. 4 Suits (Clubs, Hearts, Diamonds, Spades). 
        There are four Cards for each Value, one of each Suit. 
        """
        for val in range(2,15):
            for suit in ["Clubs", "Hearts", "Diamonds", "Spades"]:
                # create the respective Card object and add it to the list
                self.card_list.append(Card(suit, val))

    def clear(self) -> None:
        # clears the deck to reset state
        self.card_list = []
    
    def shuffle(self)-> list:
        """
        Shuffles the deck of cards to generate a random permutation and returns that list of Cards. 
        Implements the Fisher-Yates Shuffling algorithm to shuffle in place; 
        generates unbiased permutations. Does this in O(n) time.
        """
        for idx in range(len(self.card_list)-1, 0, -1):
            # grab a random index to the left of the i (since reverse iteration)
            randIdx = randint(0,idx)
            self.card_list[idx], self.card_list[randIdx] = self.card_list[randIdx], self.card_list[idx]
        return self.card_list

    def drawSingle(self) -> Card:
        """
        Pops top card off of the deck, and gives it to caller. This method can also be useful if there's custom rules regarding deck in the future. If empty deck, then return False.
        """
        result = self.card_list.pop() if self.card_list else False
        return result
    
    def splitDeck(self, num_split = 2) -> list:
        """
        Splits the card Deck by num_split times. Default split is in half (2), where each split is just half the deck.
        Returns as a list of Card lists, each Card list is one split. Cards are dealt on rotating basis to each split (player) to mimic actual dealing scenarios where deck number is not divisible by num_split.
        """
        # create list to hold all the card split lists
        wrapperList = [[] for i in range(num_split)]
        drawnCard = self.drawSingle()

        while (drawnCard): # while there are still cards in the deck
            for split in range(num_split):
                if drawnCard: # if there's a valid card
                    wrapperList[split].append(drawnCard)
                drawnCard = self.drawSingle()

        return wrapperList

            
########################################################################################################################
########################################################################################################################

#  # driver code
deck = Deck()
c = []

# checking the shuffling
# shuffled_cards = deck.shuffle()
# for c in shuffled_cards:
#     c.show()

# # checking if its split properly
# count = 0
# total = deck.splitDeck(15)
# for i in range(15):
#     print()
#     for card in total[i]:
#         count += 1
#         card.show()
#     print("count: " + str(count))
#     print()

# testing single card draw edge cases
# drawnCard = deck.drawSingle()
# if (drawnCard):
#     c.append(drawnCard)
# else:
#     print(drawnCard)

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())
# c.append(deck.drawSingle())

# drawnCard = deck.drawSingle()
# if (drawnCard):
#     c.append(drawnCard)
# else:
#     print(drawnCard)


# for card in c:
#     if card:
#         card.show()
#     else:
#         print(card)


# print(deck.card_list)