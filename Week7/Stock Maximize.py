def stockmax(prices):
    # Write your code here
    max_pr = 0
    ans = 0
    for i in range(len(prices)-1, -1, -1):
        if max_pr < prices[i]:
            max_pr = prices[i]
        ans += max_pr - prices[i]

    return ans
