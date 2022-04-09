a = "HolaQueTalHoa"

def split_capital(str):

    result = []
    temp = str[0]

    for i in range(1,len(str)):
        # print(str[i])
        if str[i].isupper():
            result.append(temp)
            temp = ''
        temp+= str[i]

    return result

print(split_capital(a))

