def findDigits(n):
    # Write your code here
    tmp = n
    ans = 0
    while tmp:
        x = tmp%10
        if x!=0 and n%x == 0:
            ans += 1
        tmp = tmp//10

    return ans
