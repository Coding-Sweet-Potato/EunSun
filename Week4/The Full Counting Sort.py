def countSort(arr):
    # Write your code here
    ans = []
    for i in range(len(arr)):
        x = int(arr[i][0])
        s = str(arr[i][1])

        if i < len(arr) // 2:
            ans.append((x, "-"))
        else:
            ans.append((x, s))

    print(" ".join(map(lambda x: x[1], sorted(ans, key=lambda x: x[0]))))
