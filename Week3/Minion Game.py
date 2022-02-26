def minion_game(string):
    # your code goes here   
    vowel = ['A', 'E', 'I', 'O', 'U']
    c_cnt = 0
    v_cnt = 0

    for j in range(len(string)):
        if string[j] in vowel:
            v_cnt += len(string)-j
        else:
            c_cnt += len(string)-j

    if v_cnt > c_cnt:
        print('Kevin '+str(v_cnt))
    elif c_cnt > v_cnt:
        print('Stuart '+str(c_cnt))
    else:
        print('Draw')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
