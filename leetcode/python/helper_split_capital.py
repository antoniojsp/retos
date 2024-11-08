a = "LargeSoftwareBook"
b = "OrangeHighlighter"
c = "OregonEugene"
d = "MariaJose"

def split_capital(string:str) -> list:
    """
    (str)->[]
    """
    result = []  # holds the results
    temp = ""  # holds one section of the string being processed
    for index, variable in enumerate(string):
        if variable.isupper() and index != 0:  # if char is capital and not the timers.
            print(variable.isupper())
            result.append(temp)
            temp = ''
        temp += variable

        if index == len(string) - 1:  # checks for the end of the string and add the last part
            result.append(temp)
    print(result)
    return result


print(split_capital(c))

