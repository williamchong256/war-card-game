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


# construct the Game class
class Game(object):
  """
  Each Game has one Deck, num_players Players. Game should keep track of who's turn it is to play a Card, and if someone has won. It should also keep track of number of turns played and who won
  """
  def __init__(self, num_players:int = 2, rounds:int = 0) -> None:
      self.players = [Player(i+1) for i in range(num_players)] # initialize each Player with idx+1 as name
      self.rounds = rounds
      self.losers = []
      self.tableCards = [] # cards that are on the table, to be collected by a Player
      self.winner = None

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
    print("  Players that lost: ")
    for player in self.losers:
      print("    Player {}".format(player.name))
    print("\n  Total number of rounds played: {}\n".format(self.rounds))

    def checkWin(self) -> bool:
      """
      Checks each Player's hand count to see if they have won (52 cards in their hand). If win, set
      self.winner to the Player and return true, else return false.
      """
      for p in self.players:
        if p.handCount == 52:
          self.winner = p
          return True
      return False

    def playTurn(self) -> None:
      """
      Method to play out a round
      """

    def run(self) -> None:
      """
      Main game loop that drives the game, prompts turns/plays, and determines if a player has won.
      """
      # checkWin() used to check if there is a winner, if no winner, then play another turn/loop
      while not checkWin(): 
        playTurn()

g = Game()
g.winner = Player(1)
g.losers = [Player(2)]
g.endGameMessage()