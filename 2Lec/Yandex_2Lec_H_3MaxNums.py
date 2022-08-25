# мой код V2
def start():
    arr = list(map(int, input().split()))

    max1 = max(arr[0], arr[1], arr[2])
    max2 = max(min(arr[0], arr[1]), min(arr[0], arr[2]), min(arr[2], arr[1]))
    max3 = min(arr[0], arr[1], arr[2])
    min1 = min(min(arr[0], arr[1]), min(arr[0], arr[2]), min(arr[2], arr[1]))
    min2 = max(min(arr[0], arr[1]), min(arr[0], arr[2]), min(arr[2], arr[1]))

    for i in range(3, len(arr)):
        if arr[i] >= max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i] >= max2:
            max3 = max2
            max2 = arr[i]
        elif arr[i] >= max3:
            max3 = arr[i]

        if arr[i] <= min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] <= min2:
            min2 = arr[i]

    if max2 * max3 * max1 > min1 * min2 * max1:
        print(max1, max2, max3)
    else:
        print(max1, min1, min2)


if __name__ == '__main__':
    start()
