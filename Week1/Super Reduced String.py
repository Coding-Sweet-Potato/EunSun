def superReducedString(s):
    # Write your code here
    flag = 1
    while flag:
        result = ''
        idx = 0
        while idx < len(s):
            if idx == len(s) - 1:
                result += s[idx]
                break
            if s[idx] != s[idx + 1]:
                result += s[idx]
            else:
                idx += 1
            idx += 1

        if len(result) == 0:
            result = 'Empty String'
            break
        
        idx = 1 #check
        flag = 0
        while idx < len(result):
            if result[idx-1] == result[idx]:
                flag = 1
                break
            idx += 1
        if flag == 1:
            s = result[:]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
