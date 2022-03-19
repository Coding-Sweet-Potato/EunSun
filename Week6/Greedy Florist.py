def getMinimumCost(k, c):
    c.sort()

    ans = 0
    i = 0

    while i < len(c):
        previous = i // k
        ans += (previous + 1) * c[len(c)-1-i]
        i += 1

    return ans
