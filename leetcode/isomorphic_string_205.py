class Solution:

    @staticmethod
    def dict_index(s:str) -> dict:
        seen_dict = {}
        for index, char in enumerate(s):
            if char not in seen_dict:
                seen_dict[char] = []
            seen_dict[char].append(index)

        return seen_dict

    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        print(list(zip(s, t)))
        print(set(zip(s, t)))
        s_index = self.dict_index(s)
        t_index = self.dict_index(t)

        for i, j in zip(s,t):
            if s_index[i] != t_index[j]:
                return False

        return True







print(Solution().isIsomorphic(s = "abc", t = "ght"))