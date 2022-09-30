def add_or_update(dic, symbol, count):
    if symbol not in dic:
        dic[symbol] = 0

    dic[symbol] += count


def start():
    n, k = map(int, input().split())
    arr = input()

    maxL = 0
    startL = 0
    dic = {}
    last = 0

    for i in range(0, len(arr)):
        add_or_update(dic, arr[i], 1)
        if dic[arr[i]] > k:
            while dic[arr[i]] > k and last < i:
                add_or_update(dic, arr[last], -1)
                last += 1

        if i - last + 1 > maxL:
            startL = last + 1
            maxL = i - last + 1

    print(maxL, startL)


if __name__ == '__main__':
    start()
