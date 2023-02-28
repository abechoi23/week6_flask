# In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in the string. If there is no such letter in the string, then the function should return -1. If the letter occurs only once in the string, then -1 should also be returned.
# Examples:
# second_symbol('Hello world!!!','l') --> 3
# second_symbol('Hello world!!!', 'A') --> -1

def second_symbol(a_string, letter):
    count= 0
    for i in range(len(a_string)):
        print(i)
        if a_string[i].lower() == letter.lower():
            count+= 1
        if count == 2:
            return i
    return -1
print(second_symbol('Hello World!!!', 'l'))



def second_symbol(s, symbol):
    r = s.lower()
    return r.find(symbol, r.find(symbol)+2)
print(second_symbol('HelLo world!!!','l'))