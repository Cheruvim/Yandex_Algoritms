def start():
    arr = []
    arr.append(int(input()))
    arr.append(int(input()))
    arr.append(int(input()))
    xHole = int(input())
    yHole = int(input())

    arr.sort()
    if arr[0] <= min(xHole, yHole) and arr[1] <= max(xHole, yHole):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    start()
