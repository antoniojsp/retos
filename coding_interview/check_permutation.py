example1 = "abab"
example2 = "abbd"


def counter(string: str) -> dict:
    temp = {}

    for i in string:
        if i not in temp:
            temp[i]= 1
        else:
            temp[i]+= 1
    return temp


def check_permutation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    dict1 = counter(string1)
    dict2 = counter(string2)

    for i, j in dict1.items():

        if i in dict2:
            if j != dict2[i]:
                return False
    return True


def check_permutation_1(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    temp1 = sorted(list(string1))
    temp2 = sorted(list(string2))

    for i, j in zip(temp1, temp2):
        if i != j:
            return False
    return True


print(check_permutation_1(example1, example2))