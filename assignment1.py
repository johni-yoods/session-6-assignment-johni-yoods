import random
from collections import Counter

value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

#1 list comprehension
def generate_deck(suits:list,value:list)->list:
    '''
    This function takes suits and value list, combines them and returns the deck
    # Input :
        suits: list
        value: list
    # Functionality:
        Iterates over suits and value and combines each value.

    # Returns:
        A list is returned containing the result of combination of value and suits.
    '''
    deck = [i+' ' + j for i in value for j in suits]
    return deck

deck = generate_deck(suits, value)
print(deck)

#2 Normal Function
def generate_deck_normal(suits, value):
    '''
    This function takes suits and value list, combines them and returns the deck
    # Input :
        suits: list
        value: list
    # Functionality:
        Iterates over suits and value and combines each value.
    
    # Returns: 
        A list is returned containing the result of combination of value and suits.
    '''
    mydeck = []
    for i in value:
        for j in suits:
            mydeck.append(i + " " + j)
    return mydeck

print(generate_deck_normal(suits,value))


#3 poker game

conv_value = {"jack":11,"queen":12,"king":13,"ace":14}
def check_cards(user_set:list):
    """ 1. first check if the colors of all the cards are same or not
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
            3. else we return 10, max(hand)"""
    value_set = []
    suit_set = []
    for i in user_set:
        value,suit = i.split()
        if value in conv_value:
            value_set.append(int(conv_value[value]))
        else:
            value_set.append(int(value))
        suit_set.append(suit)

    user_point=0
    if(len(set(suit_set))==1):  #check same suit of not. If yes its a flush
        value_set1 = value_set.copy()
        value_set1.sort()
        values = list(range(min(value_set1),max(value_set1)+1))
        print(value_set1,values)
        if(value_set1 == values): #check values are in sequence or not
            if len(value_set) == 5:
                if str(",".join(map(str,sorted(value_set1,reverse=True)))) == "14,13,12,11,10":
                    return 1,14 #royal flush
                else:
                    return 2, max(value_set1) #straight flush
            elif len(value_set) == 4:
                if str(",".join(map(str,sorted(value_set1,reverse=True)))) == "14,13,12,11":
                    return 1,14 #royal flush
                else:
                    return 2, max(value_set1) #straight flush
            elif len(value_set) == 3:
                if str(",".join(map(str,sorted(value_set1,reverse=True)))) == "14,13,12":
                    return 1,14 #royal flush
                else:
                    return 2, max(value_set1) ##straight flush 
        else:
            return 5, max(value_set1) #flush
    else:
        value_set1 = value_set.copy()
        value_set1.sort()
        values = list(range(min(value_set1),max(value_set1)+1))
        if(value_set1 == values): #check values are in sequence or not
            return 6,max(value_set) #straight
        else:
            count = dict(Counter(value_set))
            count = {i: j for i, j in sorted(count.items(), key=lambda item: item[1],reverse =  True)}
            if len(value_set) == 5:
                key1 = list(count.keys())[0]
                key2 = list(count.keys())[1]
                print("cc",count[key2])
                if count[key1] == 4:
                    return 3, key1 #4 of a kind
                elif count[key1] == 3:
                    if count[key2] == 2:
                        return 4, key1 #Full house
                    else:
                        return 7, key1 #3 of a kind
                elif count[key1] == 2:
                    if count[key2] == 2:
                        return 8, max(key1,key2)  #Two pair
                    else:
                        return 9, key1 #One pair
                else:
                    return 10,max(value_set) #High card

            elif len(value_set) == 4:
                key1 = list(count.keys())[0]
                if count[key1] == 4:
                    return 3, key1 #4 of a kind
                elif count[key1] == 3:
                    return 7, key1  #3 of a kind
                elif count[key1] == 2:
                    key2 = list(count.keys())[1]
                    if count[key2] == 2:
                        return 8, max(key1,key2)  #Two pair
                    else:
                        return 9, key1 # One pair
                else:
                    return 10,max(value_set)  #High Card
            elif len(value_set) == 3:
                key1 = list(count.keys())[0]

                if count[key1] == 3:
                    return 7, key1  #3 of a kind
                elif count[key1] == 2:
                    key2 = list(count.keys())[1]
                    return 9, key1  #One pair
                else:
                    return 10,max(value_set)   #High card


set1=[]
set2=[]
no_of_cards = 5 #no of cards each player should have

deck_2 = deck.copy()
random.shuffle(deck_2) #shuffle the deck
for i in range(no_of_cards):
    set1.append(deck_2.pop())
    set2.append(deck_2.pop())

print("player 1 cards:",set1)
print("player 2 cards:",set2)



#check who wins

a,b = check_cards(set1)
c,d = check_cards(set2)
print("Player 1 hand rating:",a,b)
print("Player 2 hand rating:",c,d)

def who_won(a:int,b:int,c:int,d:int)->int:
    """1.check if the first element is greater of player 1 than player 2, then player  wins else vice versa.
    2. if both have same, then we check the max value, i.e. the second element,
    so here if the second element of player 2 is more than the first player then second player wins and vice versa
    3. if both the players have same secopnd value, then the game ends in a draw.
    """
    if a<c:
        print("Winner is player 1")
        return 1
    elif a>c:
        print("Winner is player 2")
        return 2
    elif a == c:
        if b>d:
            print("Winner is player 1")
            return 1
        elif b<d:
            print("Winner is player 2")
            return 2
        elif b==d:
            print("It is a draw!!")
            return 0
who_won(a,b,c,d)
