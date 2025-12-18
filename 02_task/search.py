def binary_search(arr: list[float], x: float):
    size = len(arr)

    low = 0
    high = size-1
    num = 0
    last_higher = -1

    while low <= high:
        num += 1
        middle = (low + high) // 2
        middle_val = arr[middle]

        if middle_val < x:
            low = middle + 1
        elif middle_val >= x:
            last_higher = middle
            high = middle - 1
        else:
            return (num, middle_val)

    if last_higher != -1:
        return (num, arr[last_higher])

    return (num, None)

