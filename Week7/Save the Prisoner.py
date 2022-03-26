def saveThePrisoner(n, m, s):
    # Write your code here
    m = m % n
    if m == 0:
        m = n
    if s+m-1 > n:
        return (s+m-1)%n
    else:
        return s+m-1
