def start():
    t = list(map(int, input().split()))

    if len(t) <= 1:
        print("YES")
        return

    for i in range(1, len(t)):
        if t[i - 1] >= t[i]:
            print("NO")
            return

    print("YES")


if __name__ == '__main__':
    start()
