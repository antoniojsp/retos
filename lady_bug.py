
from collections import Counter

def is_consecutive_equal(b:str) -> bool:
    # if it's only one char string, then return false since it cannot be consecutive with an equal
    str_len = len(b)
    if str_len == 1:
        return False
    # if it's 2 char long string, they both need to need equal to ve valid
    if str_len == 2:
        return b[0] == b[1]

    for i in range(1, str_len-1):
        if i ==  1 and b[i-1] != b[i]: # check the start for "ABB.." case which would make it invalid
            return False
        elif i == str_len - 1 and b[i] != b[i+1]:
            return False
        elif (b[i-1] != b[i]) and (b[i] != b[i+1]):#
            return False

    return True

def is_unique_char(b):
    count = Counter(b)
    for i, j in count.items():
        if j == 1 and i != "_":
            return False
    return True
def happyLadybugs(b):
    """
    Check for spaces to move "_". One is enough to be able to relocate all the ladybugs. If there is no
    spaces open, the only option is that all the letters in the strings are not unique and they are consecutive
    with their equals
    """
    if "_" not in b:
        return "YES" if is_consecutive_equal(b) and is_unique_char(b) else "NO"

    return "YES" if is_unique_char(b) else "NO"

print(happyLadybugs("A"))

