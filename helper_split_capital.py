a = "LargeSoftwareBook"

def split_capital(str:str)->list:

    result = []
    temp = "" #holds one section of the string being processed

    # for i in range(1,len(str)):

    for i in enumerate(str):

        if i[1].isupper() and i[0] != 0:
            result.append(temp)
            temp = ''
        temp+= i[1]

        if i[0] == len(str)-1:
            result.append(temp)


    return result

print(split_capital(a))

