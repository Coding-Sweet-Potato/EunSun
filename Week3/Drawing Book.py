def pageCount(n, p):
    # Write your code here
    if p == 1 or p == n:
        return 0

    else:
        decide = n // 2
        if p <= decide :
            tmp = 'f'
        else:
            tmp = 'b'

        i=1
        while i <= n:
            if p == i*2 or p == i*2+1:
                break
            i += 1

        if tmp == 'f':
            return i
        else:
            return decide-i
