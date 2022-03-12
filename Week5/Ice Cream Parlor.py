def icecreamParlor(m, arr):
    # Write your code here
    for  i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return [i+1, j+1]
