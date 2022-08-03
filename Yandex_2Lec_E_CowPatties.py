def start():
    arr = []
    n = int(input())
    arr = list(map(int, input().split()))
    maxM = 0
    max = 0

    for i in range(len(arr)-1):
        if arr[i] > max:
            max = arr[i]
            maxM = 0
        elif arr[i] <= max and arr[i] > maxM and arr[i+1] < arr[i] and arr[i] % 10 == 5:
            maxM = arr[i]

    if maxM == 0:
        print(0)
        return

    betterCount = 0
    for i in range(len(arr)):
        if arr[i] > maxM:
            betterCount += 1

    print(int(betterCount + 1))


if __name__ == '__main__':
    start()
