a = "LargeSoftwareBook"


def split_capital(string:str) -> list:
    """
    (str)->[]
    """
    result = []
    temp = ""  # holds one section of the string being processed
    for i in enumerate(string):
        if i[1].isupper() and i[0] != 0:
            result.append(temp)
            temp = ''
        temp += i[1]

        if i[0] == len(string)-1:
            result.append(temp)
    return result


print(split_capital(a))

