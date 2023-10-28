

def weightedUniformStrings(s, queries):
    # Write your code here
    last_char_seen = None
    weights_set = set()
    current_value = 0
    for current_char in s:
        if not last_char_seen or last_char_seen != current_char:
            last_char_seen = current_char
            current_value = 0
        current_value += ord(current_char) - 96
        weights_set.add(current_value)

    return ["Yes" if i in weights_set else "No" for i in queries]





test = "abccddde"

print(weightedUniformStrings(test, [1,3,12,5,9,10]))