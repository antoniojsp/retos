from itertools import combinations

def check_valid_string(string:list)->bool:
    """
    string valid if none repeat consecutively
    """
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

def is_valid_after_delete(word:str, char_list:tuple) -> int:
    """
    testing.js if when the chars are delete, they form a valid string. Return its length
    """
    result = list(word)
    i = 0
    while i < len(result):
        if result[i] in char_list:
            del result[i]
        else:
            i +=1

    valid = check_valid_string(result)

    return len(result) if valid else 0



test = "beabeefeab"
def alternate(s:str) -> int:
    unique = list(set(i for i in s))
    length = len(unique)

    if len(unique) < 2:
        return 0
    if len(unique) == 2:
        return len(unique)

    # For  all the possible combination of two elements from the uniques elements
    solutions = list(combinations(unique, length-2))

    max_len = 0
    for i in solutions:
        max_len = max(is_valid_after_delete(s, i), max_len)

    return max_len


print(alternate(test))






