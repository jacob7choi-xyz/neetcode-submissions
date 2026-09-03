class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res, pacific, atlantic = [], set(), set()
        if not heights:
            return res
        def dfs(row: int, col: int, visited: set, prev_height: int) -> None:
            if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]) or (row, col) in visited or heights[row][col] < prev_height:
                return
            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
        for row in range(len(heights)):
            dfs(row, 0, pacific, 0)
        for col in range(len(heights[0])):
            dfs(0, col, pacific, 0)
        for row in range(len(heights)):
            dfs(row, len(heights[0]) - 1, atlantic, 0)
        for col in range(len(heights[0])):
            dfs(len(heights) - 1, col, atlantic,  0)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        return res