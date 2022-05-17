string = "ababa"

dictionary =  {}


for i in string:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1


def palindrome_permutation(string: str) -> bool:
    count = 0
    print(dictionary)
    for i , j in dictionary.items():
        if j % 2 == 1 and i != ' ' :
            count += 1
        if count > 1:
            return False
    return True


string = "tact toa"

def palin(string):
    dictionary = {}
    count = 0

    for i in string:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1

        if dictionary[i] % 2 == 1 and dictionary[i] != ' ':
            count += 1
        else:
            count -= 1
    print(count)

    return not count > 1

print(palin(string))


