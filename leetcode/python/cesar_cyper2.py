def caesarCipher(s, k):
    # CONSTANTS
    FIRST_LOWER = ord("a")
    FIRST_UPPER = ord("A")
    ABC_ENGLISH_LENGTH = 26
    result  = ""
    for letter in s:
        if letter.isalpha():
            abc_start = FIRST_UPPER if letter.isupper() else FIRST_LOWER
            ordinal_position = ord(letter) - abc_start
            new_position = (ordinal_position + k) % ABC_ENGLISH_LENGTH + abc_start
            result += chr(new_position)
        else:
            result += letter

    return result


