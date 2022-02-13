def sockMerchant(n, ar):
    # Write your code here
    sock = {}
    pair = 0
    for x in ar:
        if x in sock.keys() and sock[x] == 1:
            pair += 1
            sock[x] = 0
        else:
            sock[x] = 1
            
    return pair
