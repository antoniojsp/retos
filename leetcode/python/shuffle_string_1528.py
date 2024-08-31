class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if not s:
            return ""
        shuffled = [""] * len(indices)

        for i, c in enumerate(s):
            shuffled[indices[i]] = c

        return "".join(shuffled)