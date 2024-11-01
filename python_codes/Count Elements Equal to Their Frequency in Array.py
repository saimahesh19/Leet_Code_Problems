def aofi(arr):
    v = {}
    for i in range(len(arr)):
        if arr[i] in v:
            v[arr[i]] += 1
        else:
            v[arr[i]] = 1

    count = 0
    for key in v:
        if key == v[key]:
            count += 1

    return count
