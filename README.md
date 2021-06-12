# Session 6
#  Assignment 1 (Poker game)

# 
#
#
#
#

```
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
```
### The rules of the games

1. Players can get either of 3, 4 or 5 cards.
2. 2 players play the game
3. The winner is decided on the basis of the order shown below.

# Poker Hands Rankings
# 1.Royal Flush: 
This hand is the rarest in poker. It’s when you make a ten-to-ace straight all in the same suit such as A♦K♦Q♦J♦T♦

# 2.Straight Flush:
Five consecutive cards of differing suits, like 8♠7♠6♠5♠4♠, then you have a straight flush.
# 3.4-of-a-Kind: 
The name says it all! If you have all four of the same card, like A♠4♠4♣4♥4♦ then you have quads!
# 4.Full House: 
Also known as a “boat,” it’s when you have three of a kind along with a pair - for example: A♦A♣A♥J♥J♠ (three of one, two of the other)
# 5.Flush: 
There are four suits in poker (diamonds, hearts, spades, and clubs). When you have five cards all in the same suit, you have a flush. An example might be A♥J♥8♥4♥2♥
# 6.Straight: 
Five consecutive cards of differing suits, like 8♥7♣6♦5♦4♠ is a straight. An A-2-3-4-5 straight is known as a “wheel,” while 10-J-Q-K-A is called “Broadway.”
# 7.3-of-a-Kind: 
Whenever you have three of the same cards (i.e. A♠K♥5♠5♦5♣) you have three-of-a-kind. If you make three-of-a-kind with a pair in the hole and one on the board, it’s “a set.” If you make it with two on the board and one card in the hole, then it’s called “trips.”
# 8.Two Pair: 
Is when you have not one, but two pairs. The fifth card is your kicker. For instance, if you have A♣K♥5♥K♠5♦ you have kings and fives with an ace kicker.
# 9.One Pair: 
There are thirteen different cards of each suit. Whenever you match two, it’s called a pair. For example,A♦A♣7♠4♠2♣2 is a pair of aces.
# 10.High Card:
If no one can make a ranked hand (different suits, non-connected, unpaired) it comes down to your high card(s). If you have A♣Q♦9♥6♣3♦ then you have ace-queen high.


### Functions


# generate_deck
This function takes in suits and values as input and returns the combined deck using list comprehension as backend
# generate_deck_normal
This function takes in suits, values and deck as input and returns the combined deck using loops as backend

# check_cards

   1. first check if the colors of all the cards are same or not
      1. if they are same we check for sequence
         1. if sequence is same, we match it with royal flush sequence, if true we return 1,14 (1 represents the listing from the rank and 14 is the max value of the array corresponding to ace)
         2. else we return 2, max(hand) (straight flush)
      2. else we return 5, max(hand) (flush)
   2. else we check for sequence
      1. if true, then we return 6,max(hand) (straight)
      2. else we do a count of each number i.e. how many times they are being repeated and we sort them from higher to lower, then we check for length of the hand as algorithm now is specifically developed for ecah hand
         1. if length is 5
            1. we count the number of repeating elements, if a number is repeated 4 times we return 3,number (4 of a kind)
            2. else if a number is repeated 3 time, we check for the next number count
               1. if the next number count is 2, we return 4, number(having count of 3) (Full House)
               2. else we return 7, number(3 of a kind)
            3. else if the number is repeated 2 times, we check the count of the other number
               1. if the other number is also 2, we return 8, max(both the numbers) (2 pairs)
               2. else we return 9, number (1 pair)
            4. else we return 10,max(hand)
         2. if the length is 4
            1. we count the number of repeating elements, if a number is repeated 4 times we return 3,number (4 of a kind)
            2. else if a number is repeated 3 time, we return 7, number(3 of a kind) as here full house doesnt makes sense in 4 cards
            3. else if the number is repeated 2 times, we check the count of the other number
               1. if the other number is also 2, we return 8, max(both the numbers) (2 pairs)
               2. else we return 9, number (1 pair)
            4. else we return 10,max(hand)
         3. else if the number is 3:
            1. we check if a number is repeated 3 time, we return 7, number(3 of a kind)  as here full house and 4 at a time doesnt makes sense in 3 cards
            2. else if the number is repeated 2 times, we return 9,number as 2 of a kind doesnt makes sense in 3 cards
            3. else we return 10, max(hand)

# check result
1. Then once we get these tuples values, we check if the first element is greater of player 1 than player 2, then player  wins else vice versa.
2. if both have same, then we check the max value, i.e. the second element, so here if the second element of player 2 is more than the first player then second player wins and vice versa
3. if both the players have same secopnd value, then the game ends in a draw.

### TestCases
Added test case to test the respective ranking
