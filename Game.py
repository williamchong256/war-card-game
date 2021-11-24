"""
Author: William Chong
This program implements the card game War as detailed at: https://en.wikipedia.org/wiki/War_(card_game)

General structure of program, how objects/classes work with each other.
  - Game class (implemented in this module): The top level class which controls the game mechanics and has Player and Deck objects; checks for game end conditions, which Player gets the Cards, handles display of game state. 
  - Card object that holds card information and displays it: suit and rank
  - Deck class: collection of Card objects that Players draw from. This will be shuffled at the beginning of the game, and is then split evenly amongst the Players.
  - Player class: represents each Player in the game. A Player has a "hand" of cards. At the beginning of each round, each Player plays the card at the top of their hand.


There are some areas/rules in the War game description that are vague or unclear. I will briefly describe them in this section, but for more detailed explanation of the game mechanics, edge cases, and assumptions reference the README file associated with this project.

General Assumptions:
  - No suit ranking
  - Aces are high

Assumption 1:
  - Players don't get to determine order of how they place cards, or what they play

Assumption 2:
  - when in "War" scenario, if one player runs out of cards without the War scenario terminating, then they automatically forfeit the War scenario and lose the game

"""

from Card import Card
from Deck import Deck
from Player import Player
from typing import Union


# construct the Game class
class Game(object):
  """
  Each Game has one Deck, num_players Players. Game should keep track of who's turn it is to play a Card, and if someone has won. It should also keep track of number of turns played and who won.

  The run() method drives the Game interaction and calls upon playTurn() to play each turn, determining which Player wins the turn and gets the tableCards. checkWin() is used in run() to check if a Player has won the Game, at which point the endGameMessage() stats are displayed.
  """
  def __init__(self, num_players:int = 2) -> None:
      self.players = [Player(i) for i in range(num_players)] # initialize each Player with idx+1 as name
      self.rounds = 0
      self.tableCards = []     # all the cards that are on the table, to be collected by a Player
      self.tie = False         # detects if there is a tie situation (War)
      self.roundWinner = None  # the winner of a single "round" not to be confused with ...
      self.winner = None       # the winner of the whole game
      self.losers = []         # if a player loses all their cards, they are moved here, and removed from self.players
      self.deckSize = 12


  def roundsPlayed(self) -> int:
    """ End of a round is defined as when a Player collects the tableCards (one war scenario counts as one round)"""
    return self.rounds

  def endGameMessage(self) -> None:
    """
    Prints the end game message with stats such as number of turns played, which Player won, which Player(s) lost.
    """
    # ensure winner is actually a Player
    if self.winner:
      print("\nEND OF GAME\n")
      print("  Winner: Player {}\n".format(self.winner.name))
    else:
      #incorrect end condition, exit with error status 2
      exit(2)
    # print("  Players that lost: ")
    # for player in self.losers:
    #   print("    Player {}".format(player.name))
    print("  Total number of rounds played: {}\n".format(self.rounds))

  def checkWin(self) -> bool:
    """
    Checks each Player's hand count to see if they have won (52 cards in their hand). If win, set
    self.winner to the Player and return true, else return false.
    """
    for p in self.players:
      if p.handCount() >= self.deckSize:
        self.winner = p
        return True
    return False

  def dealCards(self) -> None:
    """ 
    This method creates a Deck which is shuffled, then splits it evenly to each player. Optionally, omit in driver code to run smaller, custom test cases.
    """
    # create the deck and dish it out
    deck = Deck()
    self.deckSize = 52     
    print("Created deck and splitting it amongst {} players...".format(len(self.players)))
    splitDeck = deck.splitDeck(len(self.players))
    for idx in range(len(self.players)):
      self.players[idx].collectCards(splitDeck[idx])
      print("Player {} now has {} cards.".format(self.players[idx].name, str(self.players[idx].handCount())))
    print("\n")

  def playTurn(self) -> tuple:
    """
    Method to play out a "turn", where a turn is defined as where each player plays only one card. This is in contrast to a "round" which can consist of one or more turns. In a turn, each player plays one card to the table. If their card is of greater value than the prior cards already in turnCards, then they're called the "roundWinner"
    """
    turnCards = []      # the set of cards played in a "turn" (ignores any previous cards that may be on table)
    for p in self.players: # players still in the game (losers have been removed and put in self.losers)
      played_card = p.playCard()
      if not played_card:
          # if p has no more cards to play, then remove from players, edge case, may not be used
          print("PLAYER {} HAS LOST!!!!!\n".format(p.name))
          self.players.remove(p)
          self.losers = self.losers + p
      else: # p plays the card
        print("Player {} plays " + played_card.show())
        # check to see if played_card beats other cards on turnCards
        maxVal = 0  
        # find the maxVal in turnCards
        if turnCards: 
          for tCard in turnCards:
            if maxVal < tCard.val:
              maxVal = tCard.val
        turnCards.append(played_card)
        # by here maxVal = 0 (meaning no prev card played) or is the max card val played
        if maxVal < played_card.val:
          self.roundWinner = p
    #end of turn checks
    if len(self.players) > 1:
      # more than one player left, check for ties
      firstCardVal = turnCards[0].val
      for tCard in turnCards:
        if tCard.val == firstCardVal:
          self.tie = True
        else:
          self.tie = False
    # if no tie, return the roundWinner; if tie, then False
    if self.tie:
      return (False, turnCards)
    else:
      return (self.roundWinner, turnCards)
    # return (self.roundWinner, turnCards) if not self.tie else (None, turnCards)

  def play(self) -> None:
    """
    Main game loop that drives the game, prompts turns/plays, and determines if a player has won.
    """

    
    p1cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13), Card("Hearts", 13)]
    p2cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13), Card("Hearts", 3)]

    self.players[0].collectCards(p1cards)
    self.players[1].collectCards(p2cards)

    #print(self.players[0].displayHand())
    #print(self.players[1].displayHand())
    # print("Player {} now has {} cards.".format(self.players[0].name, str(self.players[0].handCount())))
    # print("Player {} now has {} cards.".format(self.players[1].name, str(self.players[1].handCount())))



    # checkWin() used to check if there is a winner, if no winner, then play another round
    while not self.checkWin() and self.rounds < 10: 
      print("New turn beginning... \n")
      rWinner, turnCards = self.playTurn()
      self.tableCards = self.tableCards + turnCards
      while not rWinner:
        print("\tTie has occurred, War!")
        print("\tNew turn beginning... \n")
        rWinner, turnCards = self.playTurn()
        self.tableCards = self.tableCards + turnCards
      # give the roundWinner the tableCards
      self.rounds += 1
      rWinner.collectCards(self.tableCards)
      print("Round {} winner is {}".format(self.rounds, rWinner.name))
      print("They collect the cards on the table and now have {} cards in their hand.".format(rWinner.handCount()))
      # reset 
      self.tableCards = []
      self.tie = False
      self.roundWinner = None
    # end of game
    self.endGameMessage()
        

g = Game()
g.dealCards()
g.play()

# deck = Deck()
# count = 0
# total = deck.splitDeck(2)
# # for i in range(2):
# #     print()
# #     for card in total[i]:
# #         count += 1
# #         print(card.show())
# #     print("count: " + str(count))
# #     print()

# p1 = Player(str(1))
# p2 = Player(str(2))
# print(p1.handCount())
# print(p2.handCount())


# # for item in total[0]:
# #   print(item.show())
# #   p1.hand.append(item)
# #   print("hand count {}".format(p1.handCount()))
# p1.collectCards(total[0])

# print("\n\n\n")
# # for item in total[1]:
# #   print(item.show())
# #   p2.hand.append(item)
# #   print("hand count {}".format(p2.handCount()))
# p2.collectCards(total[1])

# # p1.collectCards(total[0])
# # p2.collectCards(total[1])

# print(p1.handCount())
# p1.displayHand()
# print("\n\n\n")


# print(p2.handCount())
# p2.displayHand()

# g.endGameMessage()