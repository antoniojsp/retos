from collections import Counter


def isValid(s):
    count = list(Counter(s).values())
    frequencies = set(count)

    #frequencies are the same in all chars -> YES
    if len(frequencies) == 1:
        return "YES"
    #case 2 more than 2 frequencies -> NO
    if len(frequencies) > 2:
        return "NO"
    #It's valid if only has one character that doesn't repeat since it can be deleted
    one_time_frequency = count.count(1)
    if one_time_frequency == 1:
        return "YES"
    #it has more than one character the only appears once.
    if one_time_frequency > 1 :
        return "NO"
    #check the difference between the two frequency is one, at this point the list has two values
    list_set = list(frequencies)
    if abs(list_set[0]-list_set[1]) == 1:
        return "YES"

    return "NO"



test = ["ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"]

for i in test:
    print(isValid(i))



