
import sys

def surround(l_res, to_deter):
    for each in l_res:
        if each[0] == to_deter[0] - 1 and each[1] == to_deter[1] - 1:
            return True
        if each[0] == to_deter[0] - 1 and each[1] == to_deter[1]:
            return True
        if each[0] == to_deter[0] - 1 and each[1] == to_deter[1] + 1:
            return True
        if each[0] == to_deter[0] and each[1] == to_deter[1] - 1:
            return True
        if each[0] == to_deter[0] and each[1] == to_deter[1] + 1:
            return True
        if each[0] == to_deter[0] + 1 and each[1] == to_deter[1] - 1:
            return True
        if each[0] == to_deter[0] + 1 and each[1] == to_deter[1]:
            return True
        if each[0] == to_deter[0] + 1 and each[1] == to_deter[1] + 1:
            return True
    
    return False

def connectedCell(matrix, n, m):
    # Complete this function
    cell = []
    res = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                cell.append((i, j))
    if len(cell) != 0:
        length = 1
    else:
        return 0
    for i in range(1, len(cell)):
        if surround(cell[:i], cell[i]):
            length += 1
        else:
            res.append(length)
            length = 1
    res.append(length)
    return max(res)

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    matrix = []
    for matrix_i in range(n):
       matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
       matrix.append(matrix_t)
    result = connectedCell(matrix, n, m)
    print(result)
