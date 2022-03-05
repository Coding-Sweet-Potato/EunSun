def closestNumbers(arr):
    # Write your code here
    out = []
    min_diff = 10**8
    arr = sorted(arr)

    for i in range(len(arr)-1):
        j = i+1
        if abs(arr[i] - arr[j]) == min_diff:
            out.append(arr[i])
            out.append(arr[j])
        if abs(arr[i] - arr[j]) < min_diff:
            out = []
            min_diff = abs(arr[i] - arr[j])
            out.append(arr[i])
            out.append(arr[j])
    return out
