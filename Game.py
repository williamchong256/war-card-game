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

Assumption 3:
  - If all other players have no cards, the remaining player wins automatically.

Assumption 4:
  - When dealing, if deck is not divisible by the number of players, then the remaining "extra" cards are dealt out circularly in order. 
  
Definitions of terms:
  - "Tie": when all the played cards in a Turn are of equal value. In this scenario, the cards remain on the table and the turn resets to determine the Round winner.
  - "Turn": In a turn, each player only plays one card to the table. If their card is of greater value than the prior cards already in turnCards, then they're called the "roundWinner"
  - "Round": can consist of multiple turns, depending on if there was a Tie scenario or not. The round is finished when one player's played card is higher than the rest of the cards played in that Turn. After this, that player takes all the cards on the table.

"""

from Card import Card
from Deck import Deck
from Player import Player
from typing import Union
import math


# construct the Game class
class Game(object):
  """
  Each Game has one Deck, num_players Players. Game should keep track of who's turn it is to play a Card, and if someone has won. It should also keep track of number of turns played and who won.

  The run() method drives the Game interaction and calls upon playTurn() to play each turn, determining which Player wins the turn and gets the tableCards. checkWin() is used in run() to check if a Player has won the Game, at which point the endGameMessage() stats are displayed.
  """
  def __init__(self, num_players:int = 2) -> None:
      self.num_players = num_players
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
    Then exits with code 0. Exiting here prevents edge cases from manifesting in nasty bugs (infinite loops)
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
    exit(0)  # need to terminate game here to prevent edge cases

  def checkWin(self) -> bool:
    """
    Checks each Player's hand count to see if they have won (52 cards in their hand). If win, set
    self.winner to the Player and return true, else return false.
    """
    if len(self.players) == 1:
      self.winner = self.players.pop()
      return True
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
      self.players[idx].collectCards(splitDeck[idx], reverse=False)
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
        print("\n  Player {} is out of cards and has LOST!\n".format(p.name))
        self.players.remove(p)
        self.losers.append(p)
        if self.num_players - len(self.losers) == 1:
          self.winner = self.players.pop()
          self.endGameMessage()
            
      else: # p plays the card
        print("  Player {} plays ".format(p.name) + played_card.show())
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
    if len(self.players) > 1 and turnCards:
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

  def play(self, round_limit:int = math.inf, custom_test:bool = False, p1cards:list = None, p2cards:list = None) -> None:
    """
    Main game loop that drives the game, prompts turns/plays, and determines if a player has won.
    Input parameters: 
    - round_limit: number of rounds to play, defaults to inf 
    - custom_test: boolean flag to determine if there are custom hand inputs
    - p1cards and p2cards: list of Cards, the custom hand inputs for p1 and p2
    """

    # check if there's a custom_test flag set, indicating want to have custom player hands    
    if custom_test:  
      print("Dealing custom test cards")
      self.players[0].collectCards(p1cards, reverse=False)
      self.players[1].collectCards(p2cards, reverse=False)
      self.deckSize = len(p1cards) + len(p2cards)

      print("Player 0 has {} cards and starts with:".format(str(self.players[0].handCount())))
      print(self.players[0].displayHand())
      print("\n\n")
      print("Player 1 has {} cards and starts with:".format(str(self.players[1].handCount())))
      print(self.players[1].displayHand())
      print("")
      print("\n\n")
    else:
      self.dealCards()

    # checkWin() used to check if there is a winner, if no winner, then play another round
    while not self.checkWin() and self.rounds < round_limit: 
      self.rounds += 1

      print("Beginning of Round {}".format(self.rounds))
      for p in self.players:
        print("  Player {} has {} cards".format(p.name, p.handCount()))
      print("\n  Playing cards... \n")
      
      rWinner, turnCards = self.playTurn()
      self.tableCards = self.tableCards + turnCards  # add cards from turn to tableCards
      while self.tie or (not rWinner):
        print("\tTie has occurred, War!")
        # for p in self.players:
        #   print("  Player {} has {} cards".format(p.name, p.handCount()))
        print("\n\tKeep playing... \n")
        rWinner, turnCards = self.playTurn()
        self.tableCards = self.tableCards + turnCards
      # give the roundWinner the tableCards
      rWinner.collectCards(self.tableCards) 
      print("\n  Round {} winner is Player {}".format(self.rounds, rWinner.name))
      print("  They collect the cards on the table and now have {} cards in their hand.\n\n".format(rWinner.handCount()))
      # reset 
      self.tableCards = []
      self.tie = False
      self.roundWinner = None
    # end of game
    self.endGameMessage()
        


## driver code, tests

g = Game(num_players=2)

# TEST CASE 1: testing that game properly handles War tie scenario, and properly terminates at end
# p1cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13), Card("Hearts", 13)]
# p2cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13), Card("Hearts", 3)]

# TEST CASE 2: testing that game properly handles when one player runs out of cards during a Tie. Expected that they should lose immediately
# p1cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13), Card("Hearts", 13)]
# p2cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13)]

# TEST CASE 3: testing that game properly handles when one player has more cards than the other 
# where p1 expected to win, after a few rounds.
# should also show that the Player's hand doesn't just wrap back to original starting card, instead we want to emulate
# real-life picking up of "stack" of cards from table, where the most recently placed card is placed top into our hand.
# this prevents circular repetition of hands, and deadlock scenarios
# p1cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13), Card("Hearts", 13)]
# p2cards = [Card("Clubs", 14), Card("Hearts", 14), Card("Spades", 14), Card("Diamonds", 14), Card("Clubs", 13), Card("Hearts", 2), Card("Hearts", 3)]

# custom run case
# g.play(custom_test=True, p1cards=p1cards, p2cards=p2cards)

# default run case
g.play(custom_test=False)
