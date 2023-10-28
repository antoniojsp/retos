

def weightedUniformStrings(s, queries):
    # Write your code here
    current = None
    weight = set()
    count = 0
    for i in s:
        if not current or current != i:
            current = i
            count = 0
        count += ord(i) - 96
        weight.add(count)

    return ["Yes" if i in weight else "No" for i in queries]





test = "abccddde"

print(weightedUniformStrings(test, [1,3,12,5,9,10]))