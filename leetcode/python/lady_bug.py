from collections import Counter

def is_consecutive_equal(b:str) -> bool:
    # if it's only one char string, then return false since it cannot be consecutive with an equal
    if len(b) == 1:
        return False
    # if it's 2 char long string, they both need to need equal to ve valid
    if len(b) == 2:
        return b[0] == b[1]

    for i in range(1, len(b)-1):
        #edge cases: check start and end to look for patters like AAB.. or BBC which would make it false
        if i ==  1 and b[i-1] != b[i]:
            return False
        elif i == len(b)-2 and b[i] != b[i+1]:
            return False
        elif (b[i-1] != b[i]) and (b[i] != b[i+1]):
            return False
    return True

def has_unique_char(b):
    '''
    checks if the string has a letter that just appear once.
    If we have a single Ladybug, then it would never could fulfill
    the property of "happy ladybug". We remove "_" to simplify code.
    '''
    count = Counter(b.replace("_",""))
    return not all(False if val == 1 else True for val in count.values())

def happyLadybugs(b):
    """
    Check for spaces to move "_". One is enough to be able to rellocate all the ladybugs. If there is no
    spaces open, the only option is that all the letters in the strings has at least 2 instances and they are consecutive with their equals
    """
    if "_" not in b:
        return "YES" if is_consecutive_equal(b) and not has_unique_char(b) else "NO"

    return "YES" if not has_unique_char(b) else "NO"