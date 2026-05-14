def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))
        board[r][c] = temp
        return found
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

if __name__ == "__main__":
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    assert exist(board, "ABCCED") == True
    assert exist(board, "SEE") == True
    assert exist(board, "ABCB") == False
    print("All tests passed!")
