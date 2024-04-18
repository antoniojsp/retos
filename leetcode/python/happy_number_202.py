class Solution:
    def isHappy(self, n: int) -> bool:

        i = 0
        seen = set()
        '''
        To detect a loop, we need to find repeated work. if a solutiuon gives us a number we have
        already seen, then it means it will loop forever. we set a "seen" set where we storage all
        the values we have procesed to find repeated work, if we do, we return false. 
        If we get a result of 1, then we return true.
        '''
        while n > 1:
            result = 0
            # while n > 0:
            #     digit = n % 10
            #     n = n - digit
            #     n //= 10
            #     result += digit ** 2
            value = str(n)
            for i in value:
                result += int(i)**2

            if result in seen:
                return False

            seen.add(result)
            n = result


        return n == 1