'''
# A program to detect if a string is a pangram

data = "the quick brown fox jumps over the lazy dog"

alphabet = "abcdefghijklmnopqrstuvwxyz"

splitAlphabet = list(alphabet)

isPangram = True

for i in splitAlphabet:
    if data.find(i) == -1:
        isPangram = False
        break

print(isPangram)
'''

# A program to detect if a string is a pangram


'''
string = "the quick brown fox jumps over the lazy dog"

import string

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    splitAlphabet = list(alphabet)

    for i in splitAlphabet:
        if s.find(i) == -1:
            return False

    return True

'''

sti = "abcdefghijklmnopqrstuvwxyz"

import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

if is_pangram(sti) == True:
    print("mmm")
