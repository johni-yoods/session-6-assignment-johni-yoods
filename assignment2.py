import random
import math
from functools import reduce, partial
import string,requests

#1.check whether a number is a Fibonacci number or not

def fibonacci_check(number:int)->bool: 
    """
    This function takes a number as an input and check whether the number is Fibonacci or not

    # input: 
        number   : int
    
    # Returns
        bool (True if the number is fib else False)

    # Funcationality:
        A number is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square
    

    """

    z=lambda x : (True if int(math.sqrt(5*x*x + 4))*int(math.sqrt(5*x*x + 4)) ==5*x*x+4 else False) or (True if int(math.sqrt(5*x*x - 4))*int(math.sqrt(5*x*x - 4)) ==(5*x*x-4) else False)
    
    return z(number) # Returns true if n is a Fibinacci Number, else false


numbers  = [1,7,8,10]
for num in numbers:
    if (fibonacci_check(num)):
        print("Number "+str(num)+" is a finbonacci number")
    else:
        print("Number "+str(num)+" is not a finbonacci number")

# 2. List Comprehension

## 2.1

def add_list(a: list ,b: list)-> list:
    """
    This function takes two list, compares each element, if list 1 ahs even element and list
    2 has odd element then they are added else ignored

    # Input:
        a: List (Input List 1)
        b: List (Input List 2)

    # Returns:
        list: Once the addition is done, the result is stored in the list and returned.
    
    # Functionality:
        The two lists are zipped and each tuple is iterated, element 1 of the tuple is checked of 
        evens and element b of the tuple is checked for odd, if the condition is satisfied
        then they are added and the result is stored in a list.
    """

    result = [x+y for x,y in zip(a,b) if x % 2 ==0 if y % 2 != 0 ]
    return result

result = add_list([2,4,6,7],[1,3,4,5])
print("resultant list where the two lists added under the condition",result)


## 2.2

def strip_string_vowel(string:str)->str:
    """
    This function takes in string as input and checks if it contains any vowel
    if yes remove the vowels from the string and returns it
    
    # Input:
        string: str (Input string over which vowel check operation will be performed.)
    
    # Returns:
        str: string with no vowels
    
    # Functionality:
        This function iterates over the elements of the string and checks if each element 
        is in vowel list or not. if not then it adds to a list.
        the list later is then converted to string using join function.
    """
    vowels = ['a','e','i','o','u']
    result = "".join([x for x in string if x.lower() not in vowels])
    return result


print("stripped string",strip_string_vowel("johni yoods"))

## 2.3

def sigmoid(number_list:list)->list:
    """
        This function calculates sigmoid value.
        
        # Input: 
            number_list: lsit, it is the list of values whose sigmoid has to be calculated
        
        # Returns:
            lsit: This function returns the list of sigmoid value of the given list
        
        # Functionality:
            This function takes a number and performs a
            sigmoid operation over it and returns the result
    """
    return [1/(1+math.exp(-x)) for x in number_list]

n_list = [1,2,3,4]
print("sigmoids of list "+str(n_list)+" is ",sigmoid(n_list))

# 2.4

def shift_chars(string:str)->str:
    """
    This function performs an alphabatical shift of 5

    # Input:
        string: str, String over which shifts has to be done
    
    # Returns:
        str: resultant String
    
    # Funcationality:
        shift each character by 5, if it is on the bottleneck, it starts again from a.
        here only lowercase alphabets are used. so we check if the order of input character is 
        + 5 greater than order of z, then we substract 26 out of it resuling in -21 (5-26) else
        we add it directly. 
    """
    result = "".join([chr(ord(x)-26) if (ord(x)+5) > ord('z') else chr(ord(x) + 5) for x in string])
    return result

print("shifted characters:",shift_chars("tsai"))

# 3 check profanity 

def check_profanity_words(paragraph: str)-> bool:
    """
    This function is used to check if bad words are present in a paragraph or not and flag them
    
    # Input:
        paragraph: str, Input paragraph given by the user

    # Returns:
        bool: It returns True if any bad word found else returns false

    # Functionality:
        The paragraph is split into words and then each word is compared with the bad word list and 
        is being flagged, if any true flag is seen, the para is marked as toxic.
    """

    if len(paragraph.split()) < 200:
        raise ValueError("Paragraph length should be minimum 200")

    url = 'https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt'
    r = requests.get(url, allow_redirects=True)

    open('swear_wordlist.txt', 'wb').write(r.content)
    f = open("swear_wordlist.txt","r")
    bad_words = f.readlines()
    f.close()
    result = any([False if x not in bad_words else True for x in paragraph.split()])
    return result

url = 'http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt'
r = requests.get(url, allow_redirects=True)

open('alice_in_wonderland.txt', 'wb').write(r.content)
f=open("alice_in_wonderland.txt","r")
paragraph = f.read(5000)
f.close()
if(check_profanity_words(paragraph)):
    print("paragraph has swear words")
else:
    print("paragraph does not have any  swear words")


# 4 Reduce Functions

## 4.1

def add_evens(numbers:list)->int:
    """
    This function adds only even numbers in the list

    # Input:
        numbers: list, This is a list of numbers
    
    # Returns:
        int: It returns the calculated sum of the integers
    
    # Functionality:
        This function takes in list, filters out all the even number using filter and lambda 
        and then passes that list to reduce function to add all the elements of it, then the result
        is returned back.

    """
    result = reduce(lambda x,y: x + y ,filter(lambda x: (x % 2 == 0), numbers))
    return result

numbers = [1,2,3,4,5,6,7,8]
print("sum of even numbers in the list:",add_evens(numbers))

## 4.2

def biggest_char(string:str)->chr:
    """
    This function finds the biggest character in the string.

    # Input:
        mystring: list, String provided by theuser
    
    # Returns:
        chr: Biggest printable character in the string
    
    # Functionality:
        This function takes in string, and checks each element if the string with other
        to findout which is the biggest one.
    """

    result = reduce(max,string, " ")
    return result

print("biggest char in the given string is ", biggest_char("johni"))

## 4.3

def add_3rd(numbers: list)->int:
    """
    This function add every 3rd number in the list

    # Input:
        number: list, This is a list of numbers
    
    # Returns:
        int: It returns the calculated sum of the integers
    
    # Functionality:
        This function takes in list, filters out the list containing all third elements 
        and then it is added

    """
    result = reduce(lambda x,y: x + y,numbers[2::3])
    return result

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
print("sum of every 3rd number in the list ",add_3rd(numbers))

# 5

def numberplate_gen()->list:
    """
    This function is used to generate random number plates

    # Input:
        None
    
    # Returns:
        list: This function returns list of all the generated number plates.
    
    # Functionality
        The format of number plate has to be KADDAADDDD, D is digit and A is alphabet
        DD has to be in the range 10 to 99 where as DDDD has to be in the range 1000 to 9999
        AA has to be uppercase ascii character

    """
    result = ["KA"+str(random.randint(10,100))+random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase) +str(random.randint(1000,10000)) for _ in range(15) ]
    return result

print(numberplate_gen())


# 6

def number_plate(state_code:str,numberplate:int)->str:
    """
    This function is used to generate custom number plates
    
    # Input:
        state_code: str
        numberplate:int 
    
    # Returns:
        list: This function returns list of all the generated number plates.
    
    # Functionality
        The format of number plate has to be KADDAADDDD/DLDDAADDDD, D is digit and A is alphabet
        DD has to be in the range 10 to 99 where as DDDD has to be in the range 1000 to 9999, chosen by the user
        AA has to be uppercase ascii character
    """
    return state_code + str(random.randint(10,100))+random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase) +str(numberplate)

def custom_numberplate(fn,statecode:str)->str:
    """
    This function is used to create custom statewise numberplates

    # Input:
        fn: Funtion (It will be called inside the partial function)
        statecode: str
    
    # Returns:
        str: It return the numberplate in the string
    
    # Functionality:
        This function call partial function which takes function as the input and its variable as the 
        parameter. statecode is something given by the user.

    """
    f = partial(fn,numberplate = 9999)
    return f(statecode)
print("custom number plate:",custom_numberplate(number_plate,"DL"))
