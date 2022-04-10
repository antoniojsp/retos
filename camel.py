# Enter your code here. Read input from STDIN. Print output to STDOUT
def split_capital(string: str) -> list:
    """
    (str)->[]
    """
    result = []  # holds the results
    temp = ""  # holds one section of the string being processed
    for index, variable in enumerate(string):
        if variable.isupper() and index != 0:  # if char is capital and not the first.
            result.append(temp)
            temp = ''
        temp += variable

        if index == len(string) - 1:  # checks for the end of the string and add the last part
            result.append(temp.rstrip())
    # print(result)
    return result


import sys

inputData = [line for line in sys.stdin.readlines()]

for i in inputData:

    linea = i.split(";")
    string_result = ""
    operation = linea[0]  # split or combine
    option = linea[1]  # method, class, variable
    values = linea[2]  # string of values, name
    if operation == "C":  # combine
        temp = values.split()
        if option in ["M", "V"]:
            for i in range(0, len(temp)):
                if i == 0:
                    string_result += temp[i]
                else:
                    string_result += temp[i].capitalize()
            if option == "M":  # add () for methods
                string_result += "()"
        else:  # classes. All capitalize
            for i in temp:
                string_result += i.capitalize()

    else:  # split
        temp = split_capital(values)
        if option in ["C", "V"]:
            for i in temp:
                string_result += i.lower() + " "
        else:  # Method
            for i in temp:
                string_result += i.lower() + " "
            string_result = string_result[:-3]  # remove () and space

    print(string_result)


