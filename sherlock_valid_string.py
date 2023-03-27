'''
rules:
valid string
- all chars appears same number of time.
- if you can remove char at index 1 and number of character is same
'''

from collections import Counter

test = ['aabbccddeefghi', 'abcdefghhgfedecba','aabbcd']
for i in test:
    print(Counter(i))