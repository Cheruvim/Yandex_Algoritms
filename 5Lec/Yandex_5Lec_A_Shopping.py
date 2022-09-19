def start():
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    n2 = int(input())
    arr2 = list(map(int, input().split()))

    last = 0
    best = (1, 1, 10000000)
    for i in range(n1):
        last_dif = abs(arr1[i] - arr2[last])

        while last < len(arr2) and abs(arr1[i] - arr2[last]) <= last_dif:
            last_dif = abs(arr1[i] - arr2[last])
            if last_dif < best[2]:
                best = (i, last, last_dif)

            last += 1

        last -= 1

    print(arr1[best[0]], arr2[best[1]])







if __name__ == '__main__':
    start()
