class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, root = [], TrieNode()
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.is_end = True
        def dfs(row: int, col: int, node: TrieNode(), word: str) -> None:
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#' or board[row][col] not in node.children:
                return
            char = board[row][col] 
            board[row][col] = '#'
            word += char
            node = node.children[char]
            if node.is_end:
                res.append(word)
                node.is_end = False
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            board[row][col] = char
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, '')
        return res