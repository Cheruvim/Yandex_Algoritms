def start():
    n = int(input())
    dic = {}
    for i in range(n):
        w, h = map(int, input().split())
        if w not in dic:
            dic[w] = h
        else:
            dic[w] = max(dic[w], h)

    ans = 0
    for i in dic.values():
        ans += i

    print(ans)


if __name__ == '__main__':
    start()
