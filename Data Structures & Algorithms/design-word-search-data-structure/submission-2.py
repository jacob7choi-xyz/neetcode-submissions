class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, current: TrieNode()) -> bool:
            if index == len(word):
                return current.is_end
            char = word[index]
            if char == '.':
                for child in current.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in current.children:
                    return False
                return dfs(index + 1, current.children[char])
        return dfs(0, self.root)
