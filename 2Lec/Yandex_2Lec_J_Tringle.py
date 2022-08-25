def start():
    nums = int(input())
    first = float(input())
    minX = 29
    maxX = 4001
    last = first
    arr = []
    for i in range(nums - 1):
        temp = input().split()
        now = float(temp[0])
        if abs(now-last) < 10**(-6):
            continue
        if temp[1] == "closer":
            arr.append(now)
        else:
            arr.append(now * (-1))

        if arr[i] > 0:
            if arr[i] < last:
                maxTemp = (arr[i] - last) / 2 + last
                if maxX > maxTemp:
                    maxX = maxTemp
            if arr[i] > last:
                minTemp = (last - arr[i]) / 2 + arr[i]
                if minX < minTemp:
                    minX = minTemp

        if arr[i] < 0:
            arr[i] = arr[i] * (-1)
            if arr[i] > last:
                maxTemp = (arr[i] - last) / 2 + last
                if maxX > maxTemp:
                    maxX = maxTemp
            if arr[i] < last:
                minTemp = (last - arr[i]) / 2 + arr[i]

                if minX < minTemp:
                    minX = minTemp

        last = arr[i]

    if minX == 29: minX = float(30)
    if maxX == 4001: maxX = float(4000)
    print(minX, maxX)


if __name__ == '__main__':
    start()
