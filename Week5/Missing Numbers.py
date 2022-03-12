def missingNumbers(arr, brr):
    # Write your code here
    ans = []
    i = 0
    j = 0
    arr = sorted(arr)
    brr = sorted(brr)
    
    while j < len(brr):
        if arr[i] != brr[j]:
            if brr[j] not in ans:
                ans.append(brr[j])
        else:
            if i >= len(arr)-1:
                for x in range(j+1, len(brr)):
                    if brr[x] not in ans:
                        ans.append(brr[x])
                return ans
            else:
                i += 1
        j += 1
        
    return sorted(ans)
