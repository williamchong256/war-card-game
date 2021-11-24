# War Card Game

This project implements the card game War as detailed [here](https://en.wikipedia.org/wiki/War_(card_game)).

There are four modules implemented here: Game.py, Card.py, Deck.py, and Player.py. Each module implements a separate class object for clarity and modularity. 

## General structure:
  - Game class: The top level class which controls the game mechanics and has Player and Deck objects; checks for game end conditions, which Player gets the Cards, handles display of game state. Also allows for custom dealing setups, limiting the number of rounds played. Terminates after endGame condition is met.
  - Card object that holds card information and displays it: suit and rank
  - Deck class: collection of Card objects that Players draw from. This will be shuffled at the beginning of the game, and is then split evenly amongst the Players.
  - Player class: represents each Player in the game. A Player has a "hand" of cards. At the beginning of each round, each Player plays the card at the top of their hand. Player class also implements collectCard() which adds a list of cards to the end of the player's hand (reversed or normal orientation).


## Assumptions, Definitions, and Corner Cases
There are some areas/rules in the War game description that are vague or unclear. I will describe them in this section.

#### General Assumptions:
  - No suit ranking
  - Aces are high

#### Assumption 1:
  - Players don't get to determine order of how they place cards or shuffling, or what Card they play. When picking up cards from the table, they always place the most recently placed card at the end closest to the top of their hand. (imagine picking up the stack of played cards and just adding it directly to your hand)
  - the last part of the above assumption aids in preventing circular deadlocks from forming between players.

#### Assumption 2:
  - when in "War" scenario, if one player runs out of cards without the War scenario terminating, then they automatically forfeit the War scenario and lose the game

#### Assumption 3:
  - If all other players have no cards, the remaining player wins automatically.

#### Assumption 4:
  - When dealing, if deck is not divisible by the number of players, then the remaining "extra" cards are dealt out circularly in order. 

  
#### Definitions of terms:
  - "Tie": when all the played cards in a Turn are of equal value. In this scenario, the cards remain on the table and the turn resets to determine the Round winner.
  - "Turn": In a turn, each player only plays one card to the table. If their card is of greater value than the prior cards already in turnCards, then they're called the "roundWinner"
  - "Round": can consist of multiple turns, depending on if there was a Tie scenario or not. The round is finished when one player's played card is higher than the rest of the cards played in that Turn. After this, that player takes all the cards on the table.

#### Corner Case 1: When one player runs out of cards during a Tie. Expected that they should lose immediately, while other Players keep going.

#### Corner Case 2: When one player has more cards than the other; where p1 expected to win, after a few rounds.

#### Corner Case 3: When encounters a Tie, properly resolves Tie by awarding winner with all the table cards

#### Corner Case 4: Terminates correctly after one player reaches 52 cards in their hand (or however many cards in deck)


## Issues Encountered and Future Work

When implementing the Game and Player class I found some strange bugs popped up when attempting to append Card items from a list to the Player hand. Specifically it led to double indexing and cross-modification across Player objects; I found this extremely strange and couldn't quite understand what caused this, or if it was some other detail that led to it. In any case, I solved this by using list concatenation instead of naively appending items iteratively.

Another issue I encountered was dealing with edge cases in the Tie scenario. It was challenging to keep track of all the different permuations of cases that could possibly lead to win/lose conditions occurring during a Tie. To solve this I detailed each specific edge case, designed my code to become valid, and tested them. Some sample test edge cases are included in Game.py and other default test cases (just as sanity checks) are included in the other modules.

While the game behaves as expected for small numbers of players (e.g. 2 as default). There are still some minor bugs that may occur when a large number of players are populated, and in the future I should investigate further how to make this project more resilient and robust to higher demands. A possible optimization for storage and access computations would be to implement the Deck object as a shared dictionary of Card values with an additional "Owner" tag to indicate that the card is in a Player's hand. This would be more space efficient, and possibly faster lookups and insertions. It could also enable some multithreading acceleration of the shuffling algorithm, or turn calculations, etc.

With more time, I would have liked to add some interesting features to this game. The first feature I'd like to add would be to allow the players to count the cards and either add cards in normal or reverse order accordingly. This creates some form of player input to shape the outcome of their hand, and possibly counter Opposing hand builds. After this, creating an interactive mode to allow a human player(s) to play would be interesting, as well as the design of an AI computer player that optimizes their hand concatenation order. Another feature would be to implement a GUI to actually display the Table and Cards being played and take player inputs.
