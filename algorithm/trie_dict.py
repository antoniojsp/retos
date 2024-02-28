
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

    def length(self):
        return len(list(self.children.keys()))
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, string:str):
        current  = self.root
        for i in string:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]

        current.isLeaf = True

    def search(self, string:str)->bool:
        current = self.root

        for i in string:
            if i not in current.children:
                return False
            current = current.children[i]

        if current.isLeaf and current:
            return True

        return False

    def longest_prefix(self):
        current = self.root
        result = ""

        while current:
            if not current.isLeaf and current.length() == 1:
                char = list(current.children.keys())[0]
                result += char
                current = current.children[char]
            else:
                return result

        return result

    def start_with(self, val):
        current = self.root

        for i in val:
            if i in current.children:
                print(i)
                current = current.children[i]
            else:
                return False

        return True


a = Trie()
a.insert("flower")
a.insert("flor")
a.insert("flight")
print(a.start_with("fl"))