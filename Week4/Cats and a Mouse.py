def catAndMouse(x, y, z):
    x_p = abs(x-z)
    y_p = abs(y-z)

    if x_p < y_p:
        return 'Cat A'
    elif x_p > y_p:
        return 'Cat B'
    else:
        return 'Mouse C'
    
