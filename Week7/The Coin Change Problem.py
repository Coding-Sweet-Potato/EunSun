#https://www.thepoorcoder.com/hackerrank-the-coin-change-problem-solution/
def getWays(n, c):
    # Write your code here
    n_perms = [1]+[0]*n #배열들 준비하기. 0번째는 1로 채우기
    for coin in c:
        for i in range(coin, n+1): #이전 계산을 참고하며 채우기
            n_perms[i] += n_perms[i-coin]
            
    return n_perms[n]
