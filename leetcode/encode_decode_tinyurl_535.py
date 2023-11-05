import hashlib

class Codec:

    def __init__(self):
        self.code = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash = hashlib.sha256().hexdigest()[:8]
        m = f"https://leetcode.com/problems/{hash}"
        self.code[hash] = longUrl
        return m


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        hash = shortUrl[-8:]
        return self.code.get(hash, 0)


temp = Codec()
a = temp.encode("https://leetcode.com/problems/design-tinyurl")
print(a)
print(temp.decode(a))