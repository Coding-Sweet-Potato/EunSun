def timeInWords(h, m):
    # Write your code here
    number = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
        7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
            13: 'thirteen', 15:'quarter', 30: 'half'}
    m = int(m)
    if m == 0:
        ans = number[h]+" o' clock"
    else:
        if m <= 30:
            middle = " past "
            hour = number[h]
        else: # 30<m
            middle = " to "
            m = 60 - m
            hour = number[h+1]

        if m==1:
            add = " minute"
        elif m==15 or m==30:
            add = ""
        else:
            add = " minutes"

        if 20<=m<=29:
            min = 'twenty '+number[m%10]
        elif m==14 or 16<=m<=19:
            min = number[m%10]+'teen'
        else:
            min = number[m]
        ans = min + add + middle + hour

    return ans
