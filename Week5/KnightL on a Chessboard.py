def BFS(n, i, j):
    vset = set()
    vset.add((0, 0)) # 거쳐간 곳들 표시
    dest = (n - 1, n - 1) #목표지점
    stack = [(0, 0)] # 시작지점 넣기

    if i != j: #가능한 step의 경우
        step = [(i, j), (i, -j), (-i, j), (-i, -j), (j, i), (j, -i), (-j, i), (-j, -i)]
    else:
        step = [(i, i), (i, -i), (-i, i), (-i, -i)]

    count = 0
    while stack:
        count += 1
        m = len(stack)

        while m > 0:
            m -= 1
            x, y = stack.pop(0)

            for stepx, stepy in step:
                x1, y1 = x + stepx, y + stepy

                if (x1, y1) == dest: # 목표지점에 도달한 경우 count 값 바로 반환
                    return count
                if 0 <= x1 < n and 0 <= y1 < n and (x1, y1) not in vset: #체스판 안에 있고, 거치지 않은 지점인지 확인
                    vset.add((x1, y1))
                    stack.append((x1, y1))
    return -1 # 목표 지점에 도달하지 못한 채 끝난 경우


def knightlOnAChessboard(n):
    ans = [[0] * (n - 1) for _ in range(n - 1)]

    for i in range(n-1):
        for j in range(i, n-1):
            ans[i][j] = BFS(n, i + 1, j + 1)

    for i in range(n - 1): # 대각선 기준으로 반대쪽에 값 넣기
        for j in range(i + 1, n - 1):
            ans[j][i] = ans[i][j]
    return ans
