def dayOfProgrammer(year):
    # Write your code here
    
    leap = 0 #check if it's leap year
    if 1700 <= year <=1917:
        if year%4==0:
            leap = 1
        else:
            leap = 0
    elif year == 1918:
        return '26.09.1918'
    else:      
        if year%400==0:
            leap = 1
        elif year%100!=0 and year%4==0:
            leap = 1
        else:
            leap = 0

    if leap:
        return '12.09.'+str(year)
    else:
        return '13.09.'+str(year)
