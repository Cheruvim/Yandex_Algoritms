def start():
    arr = set(map(int, input().split()))
    num = int(input())
    count = 0

    while True:
        temp = num % 10
        if temp not in arr:
            count += 1
            arr.add(temp)
        num = num // 10

        if num == 0:
            break

    print(count)


if __name__ == '__main__':
    start()
