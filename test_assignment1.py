import pytest
import random
import assignment1 as as1
import os
import inspect
import re
value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
README_CONTENT_CHECK_FOR = [
    'straight flush',
    'flush',
    'straight',
    'royal flush',
    'full house',
    '4 of a kind',
    '3 of a kind',
    'high card',
    '1 pair',
    '2 pair',
    'generate_deck'
]

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(as1, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, 'You are not writing proper heading'

def test_generate_deck():
    assert as1.generate_deck(suits,value) == ['2 spades', '2 clubs', '2 hearts', '2 diamonds', '3 spades', '3 clubs', '3 hearts', '3 diamonds', '4 spades', '4 clubs', '4 hearts', '4 diamonds', '5 spades', '5 clubs', '5 hearts', '5 diamonds', '6 spades', '6 clubs', '6 hearts', '6 diamonds', '7 spades', '7 clubs', '7 hearts', '7 diamonds', '8 spades', '8 clubs', '8 hearts', '8 diamonds', '9 spades', '9 clubs', '9 hearts', '9 diamonds', '10 spades', '10 clubs', '10 hearts', '10 diamonds', 'jack spades', 'jack clubs', 'jack hearts', 'jack diamonds', 'queen spades', 'queen clubs', 'queen hearts', 'queen diamonds', 'king spades', 'king clubs', 'king hearts', 'king diamonds', 'ace spades', 'ace clubs', 'ace hearts', 'ace diamonds'],'deck is not generated properly'

def test_generate_deck_normal():
    assert as1.generate_deck_normal(suits,value) == ['2 spades', '2 clubs', '2 hearts', '2 diamonds', '3 spades', '3 clubs', '3 hearts', '3 diamonds', '4 spades', '4 clubs', '4 hearts', '4 diamonds', '5 spades', '5 clubs', '5 hearts', '5 diamonds', '6 spades', '6 clubs', '6 hearts', '6 diamonds', '7 spades', '7 clubs', '7 hearts', '7 diamonds', '8 spades', '8 clubs', '8 hearts', '8 diamonds', '9 spades', '9 clubs', '9 hearts', '9 diamonds', '10 spades', '10 clubs', '10 hearts', '10 diamonds', 'jack spades', 'jack clubs', 'jack hearts', 'jack diamonds', 'queen spades', 'queen clubs', 'queen hearts', 'queen diamonds', 'king spades', 'king clubs', 'king hearts', 'king diamonds', 'ace spades', 'ace clubs', 'ace hearts', 'ace diamonds'], 'Deck is not generated properly'

def test_check_cards_royal_flush():
    user_set = ['ace diamonds', 'king diamonds', 'queen diamonds', 'jack diamonds', '10 diamonds']
    assert as1.check_cards(user_set) == (1,14), "rank generation is not proper"

def test_check_cards_straight_flush():
    user_set = ['8 spades', '7 spades', '6 spades', '5 spades', '4 spades']
    assert as1.check_cards(user_set) == (2,8), "rank generation is not proper"

def test_check_cards_four_of_kind():
    user_set = ['4 clubs', 'ace clubs', '4 diamonds', '4 hearts', '4 hearts']
    assert as1.check_cards(user_set) == (3,4), "rank generation is not proper"

def test_check_cards_full_house():
    user_set = ['ace diamonds', 'ace clubs', 'ace hearts', 'jack hearts', 'jack spades']
    assert as1.check_cards(user_set) == (4,14), "rank generation is not proper"

def test_check_cards_flush():
    user_set = ['ace hearts', 'jack hearts', '8 hearts', '4 hearts', '2 hearts']
    assert as1.check_cards(user_set) == (5,14), "rank generation is not proper"

def test_check_cards_straight():
    user_set = ['8 hearts', '7 clubs', '6 diamonds', '5 diamonds', '4 spades']
    assert as1.check_cards(user_set) == (6,8), "rank generation is not proper"

def test_check_cards_three_of_kind():
    user_set = ['3 hearts', '9 spades', '3 clubs', '3 diamonds', 'queen hearts']
    assert as1.check_cards(user_set) == (7,3), "rank generation is not proper"

def test_check_cards_two_pair():
    user_set = ['king clubs', 'king hearts', '4 hearts', '4 spades', '5 diamonds']
    assert as1.check_cards(user_set) == (8,13), "rank generation is not proper"

def test_check_cards_one_pair():
    user_set = ['2 spades', '2 clubs', '8 clubs', 'queen hearts', 'king clubs']
    assert as1.check_cards(user_set) == (9,2), "rank generation is not proper"

def test_check_cards_high_card():
    user_set = ['queen clubs', '8 clubs', '6 spades', 'ace hearts', '10 hearts']
    assert as1.check_cards(user_set) == (10,14), "rank generation is not proper"

def test_check_draw():
    a,b,c,d=10,13,10,13
    assert as1.who_won(a,b,c,d) == 0, "winning prediction is not properly written"

def test_check_player1_win():
    a,b,c,d=9,5,10,13
    assert as1.who_won(a,b,c,d) == 1, "winning prediction is not properly written"
def test_check_player2_win():
    a,b,c,d=10,14,9,4
    assert as1.who_won(a,b,c,d) == 2, "winning prediction is not properly written"
