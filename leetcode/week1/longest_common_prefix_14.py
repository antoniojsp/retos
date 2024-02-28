from typing import List

strs = ["s","saa"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(i) for i in strs])
        result = []
        i = 0
        while i < min_len:
            temp = set()
            current = ""
            for letter in strs:
                if letter[i] not in temp:
                    temp.add(letter[i])
                current = letter[i]
            if len(temp) > 1:
                break
            i+=1

            result.append(current)
        return "".join(result)

print(Solution().longestCommonPrefix(strs))
















class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

    def return_letter(self):
        index = -1
        count = 0
        # print(self.children)
        for i in range(len(self.children)):
            if self.children[i]:
                count += 1
                index = i
            if count > 1:
                return -1
        return index


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        currently just working for lower chars
        """
        current = self.root
        for i in word:
            pox = ord(i) - 97
            if not current.children[pox]:
                current.children[pox] = TrieNode()
            current = current.children[pox]
        current.isLeaf = True

    def search(self, word):

        current = self.root

        for i in word:
            pox = ord(i) - 97
            if not current.children[pox]:
                return False
            current = current.children[pox]
        if current.isLeaf and current:
            return True

        return False

    def longest_common_prefix(self):
        current = self.root
        i = current.return_letter()
        result = ""
        while i != -1 and not current.isLeaf:
            result += chr(97 + i)
            current = current.children[i]
            i = current.return_letter()

        return result


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         trie_data_structure = Trie()
#         for i in strs:
#             if len(i) == 0:
#                 return ""
#             trie_data_structure.insert(i)
#
#         return trie_data_structure.longest_common_prefix()

