def angryProfessor(k, a):
    # Write your code here
    cnt = 0
    for x in a:
        if x <= 0:
            cnt+= 1
        if cnt == k:
            return 'NO'
    return 'YES'
