def start():
    arr = []
    arr = list(map(int, input().split()))

    max1 = -1
    max2 = -1
    min1 = 1
    min2 = 1

    for i in range(len(arr)):
        if arr[i] >= max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

        if arr[i] <= min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    if len(arr) == 2:
        print(str(min(arr[0], arr[1])) + " " + str(max(arr[0], arr[1])))
        return

    if max1 * max2 > min1 * min2:
        print(str(max2) + " " + str(max1))
    else:
        print(str(min1) + " " + str(min2))


if __name__ == '__main__':
    start()
