class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#' or board[row][col] != word[index]:
                return False
            temp = board[row][col]
            board[row][col] = '#'
            res = (
            dfs(row + 1, col, index + 1) or 
            dfs(row, col + 1, index + 1) or
            dfs(row - 1, col, index + 1) or
            dfs(row, col - 1, index + 1))
            board[row][col] = temp
            return res
        for i in range(len(board)):
            for k in range(len(board[0])):
                if dfs(i, k, 0):
                    return True
        return False