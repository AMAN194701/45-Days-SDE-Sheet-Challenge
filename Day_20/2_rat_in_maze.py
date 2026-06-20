class Solution:
    # Check whether a cell is valid to visit
    def isSafe(self, x, y, n, maze, visited):
        return (
            0 <= x < n and                 # Inside row boundary
            0 <= y < n and                 # Inside column boundary
            maze[x][y] == 1 and            # Cell is not blocked
            visited[x][y] == 0             # Cell not visited before
        )
    # backtracking function
    def solve(self, x, y, n, maze, visited, path, res):
        # Destination reached
        if x == n - 1 and y == n - 1:
            res.append(path)
            return

        # mark current cell as visited
        visited[x][y] = 1

        # Move Down
        if self.isSafe(x + 1, y, n, maze, visited):
            self.solve(x + 1, y, n, maze,
                       visited, path + "D", res)

        # Move Left
        if self.isSafe(x, y - 1, n, maze, visited):
            self.solve(x, y - 1, n, maze,
                       visited, path + "L", res)

        # Move Right
        if self.isSafe(x, y + 1, n, maze, visited):
            self.solve(x, y + 1, n, maze,
                       visited, path + "R", res)

        # Move Up
        if self.isSafe(x - 1, y, n, maze, visited):
            self.solve(x - 1, y, n, maze,
                       visited, path + "U", res)

        # Backtrack: remove current cell from path
        visited[x][y] = 0

    def findPath(self, maze, n):
        res = []

        # If starting cell is blocked
        if maze[0][0] == 0:
            return res
        visited = [[0] * n for _ in range(n)]

        # Start from (0,0)
        self.solve(0, 0, n, maze,
                   visited, "", res)
        return res

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

n = len(maze)

obj = Solution()

print(obj.findPath(maze, n))