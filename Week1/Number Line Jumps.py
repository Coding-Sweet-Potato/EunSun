def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 > x2:
        m_x, m_v = x1, v1
        s_x, s_v = x2, v2
    else:
        m_x, m_v = x2, v2
        s_x, s_v = x1, v1
    print(m_x, m_v, s_x, s_v)
    if m_v >= s_v or (m_x-s_x)%(s_v-m_v) != 0:
        result = "NO"
    else:
        result = "YES"
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
