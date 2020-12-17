# A program to replace a string of letters with their position in the alphabet
'''
data = "The narwhal bacons at midnight"
import
import string
def alphabet_position(text):
    finalArray = []
    text = text.lower()
    splitText = list(text)
    for i in splitText:
        finalArray.append(str(string.ascii_lowercase.find(i)))

    return ' '.join(finalArray)

print(alphabet_position(data))
'''

import string
data = "The narwhal bacons at midnight"

def alphabet_position(text):
    finalArray = []
    text = text.lower()
    splitText = list(text)
    print(set(string.ascii_lowercase))
    for i in splitText:
        finalArray.append(str(string.ascii_lowercase.find(i) + 1))

    return ' '.join(finalArray)

print(alphabet_position(data))