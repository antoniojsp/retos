a = "LargeSoftwareBook"


def split_capital(string:str) -> list:
    """
    (str)->[]
    """
    result = []  # holds the results
    temp = ""  # holds one section of the string being processed
    for index, variable in enumerate(string):
        if variable.isupper() and index != 0:
            result.append(temp)
            temp = ''
        temp += variable

        if variable == string[-1]: # checks for the end of the string and add the last part
            result.append(temp)
    return result


print(split_capital(a))

