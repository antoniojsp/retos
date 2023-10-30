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

        seen = {}
        for i,j in zip(s,t):
            if i not in seen:
                seen[i] = j
            elif i in seen and seen[i] != j:
                return False

        return True


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#
#         seen = {}
#         checked = set()
#         for i, j in zip(s, t):
#             if i not in seen:
#                 seen[i] = j
#                 if j in checked:
#                     return False
#                 checked.add(j)
#
#             elif seen[i] != j:
#                 return False
#
#         return True







print(Solution().isIsomorphic(s = "abc", t = "ght"))