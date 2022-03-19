def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks = sorted(sticks, reverse=True)
    ans = []
    
    def dfs(candi, start):
        if len(candi) == 3:
            if candi[0] < candi[1] + candi[2]:
                ans.append([candi[0], candi[1], candi[2]])
                return 1
            else:
                return 0
        for i in range(start+1, len(sticks)):
            candi.append(sticks[i])
            flag = dfs(candi, i)
            candi.pop()
            if flag == 0:
                break

    dfs([], -1)

    if len(ans) == 0:
        return [-1]

    max_sum = 0
    max_idx = 0
    for i in range(len(ans)):
        if sum(ans[i]) > max_sum:
            max_idx = i
            max_sum = sum(ans[i])
            
    return sorted(ans[max_idx])
