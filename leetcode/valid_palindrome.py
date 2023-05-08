from string import ascii_lowercase,digits
import re
def isPalindrome( s: str) -> bool:
    str_list = []

    for i in s:
        current_char = i.lower()
        if current_char in ascii_lowercase + "1234567890":
            str_list.append(current_char)
    return str_list == list(reversed(str_list))

def isPalindrome1( s: str) -> bool:

    # for i in s:
    #     current_char = i.lower()
    #     if current_char in ascii_lowercase + "1234567890":
    #         str_list += current_char
    str_list = re.sub(r'[^a-zA-Z0-9/]+', '', s)
    str_list = re.sub(r'([A-Z])', lambda x: x.group(0).lower(), str_list)
    print(str_list)
    for i in range(0, len(str_list)//2):
        if str_list[i] != str_list[len(str_list)-1-i]:
            return False
    return True


print(isPalindrome1("A man, a plan, a canal -- Panama"))
# import re
#
# test = "A man, a plan, a canal: Panama"
#
# test = re.sub(r'[^a-zA-Z0-9/-]+', '', test)
# test = re.sub(r'([A-Z])', lambda x: x.group(0).lower(), test)
#
# print(test)