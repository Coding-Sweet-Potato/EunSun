def birthday(s, d, m):
    ans = 0
    left_idx = 0
    right_idx = m-1
    hap = sum(s[left_idx:right_idx+1])
    
    if hap == d:
        ans += 1        
    for i in range(len(s)-m):
        left_idx += 1
        right_idx += 1
        hap = hap - s[left_idx-1] + s[right_idx]
        if hap == d:
            ans += 1
            
    return ans
