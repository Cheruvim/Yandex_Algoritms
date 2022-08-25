def start():
    n = int(input())
    arr = set()

    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x + y == n - 1 and x > -1 and y > -1 and x not in arr:
            count += 1
            arr.add(x)

    print(count)


if __name__ == '__main__':
    start()
