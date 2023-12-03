from pprint import pprint as p

class Solution:
    @staticmethod
    def counter(str):
        result = {}
        for i in str:
            if i not in result:
                result[i] = 0
            result[i] += 1

        return result

    def longestPalindrome(self, s: str) -> int:
        temp = self.counter(s)
        p(temp)
        # look for all even
        max_odd = 0;
        sum_even = 0;
        for i, j in temp.items():
            if j%2 == 1:
                max_odd = max(max_odd, j)
            if j%2 == 0:
                sum_even += j


        return max_odd + sum_even


# abceeeeeeecba

print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))