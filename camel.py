https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

# Enter your code here. Read input from STDIN. Print output to STDOUT
def split_capital(string:str) -> list:
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

        if variable == string[-1]:  # checks for the end of the string and add the last part
            result.append(temp)
    return result

while True:
    linea = input().split(";")
    print(linea)
    if linea[0] == "C":
        option = linea[1]
        if option in ["M", "V"] :
            temp = linea[2].split()
            for i in range(0, len(temp)):
                if i == 0:
                    print(temp[i], end="")
                else:
                    print(temp[i].capitalize(), end="")
            print("()")
        else:
            temp = linea[2].split()
            print("{}{}".format(temp[0].capitalize(),temp[1].capitalize()))
