def bomb(grid):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    matrix = []
    for i in range(len(grid)):
        matrix.append(list(grid[i]))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end='')
        print()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if matrix[i][j] == 'O':
                matrix[i][j] = 'X'
                for xx, yy in zip(dx, dy):
                    if 0<=i+yy<len(matrix) and 0<=j+xx<len(matrix[0]) and matrix[i+yy][j+xx] != 'O':
                            matrix[i+yy][j+xx] = 'X'
    return matrix


def bomberMan(n, grid):
    ans = []
    if n==1:
        return grid
    elif n%2==0:
        for i in range(len(grid)):
            ans.append('O'*len(grid[0]))
        return ans
    else:
        cnt = n//2
        matrix = bomb(grid)
        for i in range(len(matrix)):
            ans.append(''.join(matrix[i]).replace('.', 'O').replace('X', '.'))

        if cnt%2!=0:
            return ans
        else:
            matrix = bomb(ans)
            ans = []
            for i in range(len(matrix)):
                ans.append(''.join(matrix[i]).replace('.', 'O').replace('X', '.'))
            return ans

