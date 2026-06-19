class Solution:
    def solveNQueens(self, n: int):
        def isSafe(row, col):
            # Check left row
            for j in range(col):
                if board[row][j] == "Q":
                    return False
            # Check upper-left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check lower-left diagonal
            i, j = row, col
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1

            return True

        def backtrack(col):
            if col == n:
                ans.append(["".join(row) for row in board])
                return

            for row in range(n):

                if isSafe(row, col):
                    # Place
                    board[row][col] = "Q"
                    # Recurse
                    backtrack(col + 1)
                    # Backtrack
                    board[row][col] = "."
        board = [["."] * n for _ in range(n)]
        ans = []

        backtrack(0)

        return ans
        