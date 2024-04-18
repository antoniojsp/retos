class Solution:
    @staticmethod
    def counter(string:str) -> dict:
        result = {}
        for i in string:
            if i not in result:
                result[i] = 0
            result[i] += 1
        return result

    def longestPalindrome(self, s: str) -> int:
        # count the char frequencies of the string.
        char_freq = self.counter(s)
        sum_even = 0
        odds = 0
        for j in char_freq.values():

            # if the freq is odd, means it can produce a palindrome. We add all the chars
            if j%2 == 0:
                sum_even+= j
            # if freq odd, subtract 1, making it even and adding it to the total of chars
            # if there is one even, it we set the "odds" to 1, and add that one in the result
            elif j%2 == 1:
                sum_even += (j - 1)
                odds = 1



        return sum_even + odds


# abceeeeeeecba

print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))