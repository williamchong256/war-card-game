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