from string import ascii_letters,digits

def isPalindrome( s: str) -> bool:
    str_list = []

    for i in s:
        current_char = i.lower()
        if current_char in ascii_lowercase + "1234567890":
            str_list.append(current_char)
    return str_list == list(reversed(str_list))


