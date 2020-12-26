
def isValidSudoku(board):
    def check(l):
        already = set()
        for n in l:
            if not n == ".":
                if n in already:
                    return False
                else:
                    already.add(n)
        return True

    # row:橫
    for i in range(9):
        n = []
        for j in range(9):
            n.append(board[i][j])
        if check(n) == False:
            return False 

    # col:直
    for i in range(9):
        n = []
        for j in range(9):
            n.append(board[j][i])
        if check(n) == False:
            return False 
    # 3 * 3
    lefttop = [(0, 0), (0, 3), (0, 6),
               (3, 0), (3, 3), (3, 6),
               (6, 0), (6, 3), (6, 6)]
    for x, y in lefttop:
        # 
        n = []
        for i in range(3):
            for j in range(3):
                n.append(board[x+i][y+j])
        if check(n) == False:
            return False 
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))