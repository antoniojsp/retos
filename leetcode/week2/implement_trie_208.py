#
# class TrieNode:
#     def __init__(self):
#         self.dict = {}
#         self.isCompletes = False
#
#
# class Trie:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:
#         current = self.root
#         for i in word:
#             if i not in current.dict:
#                 current.dict[i] = TrieNode()
#             current = current.dict[i]
#         current.isCompletes = True
#     def search(self, word: str) -> bool:
#         current = self.root
#         for i in word:
#             if i not in current.dict:
#                 return False
#             current = current.dict[i]
#
#         if current.isCompletes:
#             return True
#         return False
#
#     def startsWith(self, prefix: str) -> bool:
#         current = self.root
#         for i in prefix:
#             if i not in current.dict:
#                 return False
#             current = current.dict[i]
#
#         return True
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            if i not in current:
                current[i] = {}
            current = current[i]

        current["."] = True
        print(self.root)

    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            if i not in current:
                return False
            current = current[i]
        if current["."]:
            return True

        return False

    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            if i not in current:
                return False
            current = current[i]
        if "." in current:
            return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
print(param_2)
param_3 = obj.startsWith("app")
print(param_3)