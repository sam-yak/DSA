def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    lo = 0
    hi = m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True
    print("All tests passed!")
