def countingValleys(steps, path):
    # Write your code here
    check = {'U':0, 'D':0}
    cnt = 0
    
    for x in path:
        if check['D'] == 0 and check['U'] == 0 and x=='U':
            cnt -= 1
        check[x] += 1
        if check['U'] == check['D']:
            cnt += 1
            check = {'U':0, 'D':0}
    
    if cnt < 0:
        cnt = 0
    return cnt
        
