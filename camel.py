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


while True:
    try:
        linea = input().split(";")
        # print(linea)
        result = []
        if linea[0] == "C":  # combine
            option = linea[1]
            if option in ["M", "V"]:
                temp = linea[2].split()
                # temp_result = ""
                for i in range(0, len(temp)):
                    if i == 0:
                        print(temp[i], end="")
                        # temp_result += temp[i]
                    else:
                        print(temp[i].capitalize(), end="")
                        # temp_result += temp[i].capitalize()
                if option == "M":
                    print("()")

            else:
                temp = linea[2].split()
                print("{}{}".format(temp[0].capitalize(), temp[1].capitalize()))

        else:  # split
            option = linea[1]
            if option in ["C", "V"]:
                temp = split_capital(linea[2])
                for i in temp:
                    print(i.lower(), end=" ")
                print()
            else:
                print(linea[2])
    except:
        break



