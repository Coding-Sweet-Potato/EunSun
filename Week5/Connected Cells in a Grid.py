def dfs(i, j, cnt):
    n = len(matrix)
    m = len(matrix[0])
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    matrix[i][j]=0
    cnt += 1
    
    for k in range(8):
        x = j+dx[k]
        y = i+dy[k]
        if 0<=x<m and 0<=y<n and matrix[y][x]==1:
            cnt = bfs(y, x, cnt)
    return cnt

def connectedCell(matrix):
    # Write your code here
    ans = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                cnt = dfs(i, j, 0)
                if ans < cnt:
                    ans = cnt
    return ans
