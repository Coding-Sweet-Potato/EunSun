def encryption(s):
    # Write your code here
    row = len(s)//2
    while row*(row-1) >= len(s):
        row -=1

    if row*row >= len(s):
        col = row
    else:
        col = row+1
        
    res = ''
    for i in range(col):
        res += s[i::col] +' '
        
    return res
