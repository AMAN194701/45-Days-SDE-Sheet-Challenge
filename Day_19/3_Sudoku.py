class Solution:
    def solveSudoku(self, board):
        def isValid(row, col, num):
            # Check row
            for c in range(9):
                if board[row][c] == num:
                    return False
            # Check column
            for r in range(9):
                if board[r][col] == num:
                    return False

            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num:
                        return False
            return True

        def backtrack():
            # Find empty cell
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        # check digits 1-9
                        for num in "123456789":
                            if isValid(row, col, num):
                                board[row][col] = num

                                # recurse
                                if backtrack():
                                    return True
                                # backtrack
                                board[row][col] = "."
                        # No number works
                        return False
            # No empty cells left
            return True

        backtrack()
        