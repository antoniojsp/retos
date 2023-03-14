s = "cde"

def check_palindrome(word:str):
    return word == word[::-1]

test = "abba"
def theLoveLetterMystery(s):
    # Write your code here
    count = 0
    for i in range(0, len(s)//2):
        print(s[i], s[len(s)-1-i], end="")
        count += abs(ord(s[i]) - ord(s[len(s)-1-i]))
        print()
    return count

print(theLoveLetterMystery(test))