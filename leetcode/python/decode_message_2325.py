class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        keys = ""
        seen = set()
        for i in key:
            if i not in seen and i != " ":
                keys += i
                seen.add(i)

        decoded = ""
        for i in message:
            if i != " ":
                decoded += chr(97 + keys.index(i))
            else:
                decoded += i
        return decoded

