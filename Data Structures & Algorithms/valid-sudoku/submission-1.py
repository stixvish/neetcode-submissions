class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            v = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for item in row:
                if item == ".":
                    continue
                if int(item) not in v:
                    return False
                else:
                    v.remove(int(item))
        # check cols
        for c in range(0, 9):
            v = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for r in range(0, 9):
                if board[r][c] == ".":
                    continue
                if int(board[r][c]) not in v:
                    return False
                else:
                    v.remove(int(board[r][c]))
        # check grid
        for i in range(3):    
            for j in range(3):  
                v = {1, 2, 3, 4, 5, 6, 7, 8, 9}  
                for r in range(3 * i, 3 * i + 3):
                    for c in range(3 * j, 3 * j + 3):
                        item = board[r][c]
                        if item == ".":
                            continue
                        val = int(item)
                        if val not in v:
                            return False
                        else:
                            v.remove(val)
        return True