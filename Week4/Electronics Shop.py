def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards = sorted(keyboards, reverse=True)
    drives = sorted(drives, reverse=True)
    best = 0

    for x in keyboards:
        for y in drives:
            if x+y <=b and best < x+y:
                best = x+y
                
    if best!=0:
        return best
    else:
        return -1

    for x in keyboards:
        for y in drives:
            if x+y <=b:
                return x+y   
    return -1
