def start():
    arr = []
    n = int(input())
    arr = list(map(int, input().split()))


    startMirrorLeft = -1
    currMirrirRight = 0
    mirror = False

    if len(arr) == 1:
        print(0)
        return

    for i in range(len(arr)):
        if i == len(arr) - currMirrirRight:
            break

        if arr[i] == arr[len(arr) - currMirrirRight - 1]:
            if not mirror:
                startMirrorLeft = i

            mirror = True
            currMirrirRight += 1
        else:
            currMirrirRight = 0
            startMirrorLeft = -1
            mirror = False

    count = startMirrorLeft
    print(count)
    arrAd = []
    for i in range(startMirrorLeft-1, -1, -1):
        print(arr[i], end=" ")


if __name__ == '__main__':
    start()
