def start():
    arr = []

    n = int(input())
    arr = list(map(int, input().split()))

    x = int(input())

    curr = arr[0]
    currMin = x - curr
    if currMin < 0: currMin *= (-1)

    for i in range(len(arr)):
        temp = arr[i] - x
        if temp < 0:
            temp *= (-1)

        if temp < currMin:
            curr = arr[i]
            currMin = temp

    print(curr)

if __name__ == '__main__':
    start()
