
def process_data(file:str)->dict:
    """
    function that process a text file that encodes a secret message
    it read line by line and storage it in a dictionary using
    the number as a key and the string as value
    """
    with open(file) as file:
        lines = file.readlines()
    input_code:dict = {}
    for line in lines:
        if line != "\n":
            key, string = line.split(" ")  # it cleans the string from the escape character
            input_code[int(key)] = string.strip()
    return input_code


def decode(message_file:str)->str:
    """
    function that creates a sequence of values following the pyramid structure to decode the message
    """
    secret_code:dict = process_data(message_file)
    print(secret_code[3])
    level:int = 1  # starting point
    step:int = 2  # first step
    result:list = []
    while level in secret_code:
        result.append(secret_code[level])
        level += step
        step += 1
    return " ".join(result)

print(decode("sample.txt"))



# Solution A would work correctly if the input array were exactly three items long. Fewer elements than that would create an "out of order" exception, and more than 3 elements would leave unchecked elements after the third element.
# Solution C has a similar issue (it would only work with three elements long arrays), and also,  doesn't show where the variables "word1", "word2" and "word3" were declared.
# Solution B works the best since it has no syntax error and works fine with an array of any size.
#
# All
# three
# functions
# would
# give
# us
# the
# right
# answer, but
# function
# A is the
# most
# efficient, Function
# B
# would
# check
# all
# the
# numbers
# from
#
# 1
# to
# n
# to
# find
# all
# those
# that
# are
# primes, making
# the
# function
# time
# complexity
# of
# O(n), at
# the
# same
# time, the
# array
# "factors"
# contains
# all
# the
# number
# from
#
# 2
# to
# n, which
# would
# make
# the
# space
# complexity
# of
# this
# function
# 0(n).
# Function
# C
# doesn
# 't need extra space but it checks all values from 1 to n, which time complexity O(n),
# Finally, function
# A
# uses
# the
# fact
# that
# the
# greater
# dividend
# of
# a
# number is its
# square
# root, so
# it
# checks
# from
#
# 2
# to
# the
# square
# root
# of
# n, making
# it
# a
# 0(sqrt(n))
# function, hence, more
# efficient
# than
# the
# other
# two
# functions.
#
#
# The AI gives a contradictory answer in response B. It's claiming that it's not ethically correct to access someone's system but, at the same time, it gives them specific instructions of how to do it.
# Response A is the best response since it only explains its reasoning for not providing that information.
#
# In
# response
# A, there is a
# bug
# with the list "subsets".It gets redeclared with every loop, eliminating all previous work and making it unable to provide the right answer.Response B is the correct implementation of the function.