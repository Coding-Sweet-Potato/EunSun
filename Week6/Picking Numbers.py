def pickingNumbers(a):
    # Write your code here
    ans = 0
    tmp = 0
    set_a = set(a)

    for x in set_a:
        for i in range(len(a)):
            if 0 <= a[i]-x <= 1:
                tmp += 1

        if ans <= tmp:
            ans = tmp
        tmp = 0

    return ans
