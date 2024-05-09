class Solution:

    @staticmethod
    def precompute_compress_values(chars:list)->list:
        left = 0
        right  = left + 1
        result = []
        count = 1
        while right < len(chars):
            if chars[left] == chars[right]:
                count+=1
                right+=1
            else:
                result.append((chars[left], count))
                count= 1
                left = right
                right = left +1
        else:
            result.append((chars[left], count))
        return result


    @staticmethod
    def transfer_to_chars_and_count(chars:list, result:list)->int:
        k = 0
        count = 0
        for char, times in result:
            if times == 1:
                chars[k] = char
                k+=1
                count+=1
            elif times < 10:
                chars[k], chars[k+1] = char, str(times)
                k+=2
                count+=2
            else:
                chars[k]=char
                k+=1
                count+=1
                for i in str(times):
                    chars[k] = i
                    k += 1
                    count+=1
        return count

    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        result = self.precompute_compress_values(chars)
        count = self.transfer_to_chars_and_count(chars, result)

        return count