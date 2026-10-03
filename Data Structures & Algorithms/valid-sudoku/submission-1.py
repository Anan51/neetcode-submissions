class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            print(i)
        n = len(board)
        seen = set()
        for i in board:
            for j in i:
                if j in seen and j.isdigit():
                    return False
                else:
                    seen.add(j)
            seen = set()
        seen = set()
        for i in range(n):
            for j in range(n):
                if board[j][i] in seen and board[j][i].isdigit():
                    return False
                else:
                    seen.add(board[j][i])
            seen = set()
        seen = set()
        for i in range(n):
            for j in range(n):
                if board[j][i] in seen and board[j][i].isdigit():
                    return False
                else:
                    seen.add(board[j][i])
            seen = set()
        
        for i in range(0,n,3):
            for j in range(0,n,3):
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] in seen and board[i+k][j+l].isdigit():
                            return False
                        else:
                            seen.add(board[i+k][j+l])
                seen = set()

        return True