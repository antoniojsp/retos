#https://www.hackerrank.com/challenges/taum-and-bday/problem

"""
check diff between value of white gift and black gift

"""
from collections import namedtuple


# b, w = 3, 6
# bc = 9
# wc = 1
# z = 1


b, w = 3,6
bc = 9
wc = 1
z = 1

if abs(bc - wc) <= z:
    result = b*bc + w*wc
else:


