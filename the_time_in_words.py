numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
           10: 'ten', 11: 'eleven', 12 : 'twelve',13: 'thirteen',
           14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen',
           18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one',
           22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
           26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'
           }

h = 5
m = 59

result = ""

if m == 00:
    result = f"{numbers[h]} o' clock "
elif m == 1:
    result = f"{numbers[m]} minute past {numbers[h]}"
elif m == 15:
    result = f"{numbers[m]} past {numbers[h]}"
elif m < 30:
    result = f"{numbers[m]} minutes past {numbers[h]}"
elif m == 30:
    result = f"half past {numbers[h]}"
else:
    minutes = 60 - m
    if minutes == 1:
        result = f"{numbers[minutes]} minute to {numbers[h+1]}"
    elif minutes == 15:
        result = f"{numbers[minutes]} to {numbers[h+1]}"
    else:
        result = f"{numbers[minutes]} minutes to {numbers[h+1]}"

print(result)


