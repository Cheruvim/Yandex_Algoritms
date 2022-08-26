def start():
    n = int(input())
    arr = set()

    for i in range(n):
        x, y = map(int, input().split())
        arr.add(x)
    print(len(arr))


if __name__ == '__main__':
    start()
