def start():
    arr = []
    n = int(input())
    arr = list(map(int, input().split()))


    startMirrorLeft = -1
    currMirrorRight = 0
    mirror = False

    if len(arr) == 1:
        print(0)
        return

    for i in range(len(arr)):
        if arr[len(arr) - 1] == arr[i]:
            for j in range(i, len(arr)):
                if i == len(arr) - currMirrorRight - 1:
                    break
                if arr[j] == arr[len(arr) - currMirrorRight - 1]:
                    if not mirror:
                        startMirrorLeft = i

                    mirror = True
                    currMirrorRight += 1
                else:
                    currMirrorRight = 0
                    startMirrorLeft = -1
                    mirror = False
                    break
        if mirror:
            break

    if startMirrorLeft == -1:
        startMirrorLeft = len(arr) - 1
    print(startMirrorLeft)
    for i in range(startMirrorLeft-1, -1, -1):
        print(arr[i], end=" ")


if __name__ == '__main__':
    start()
