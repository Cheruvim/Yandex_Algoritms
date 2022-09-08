def start():
    t, d, n = map(int, input().split())

    res = [(0, 0)]
    for i in range(n):
        x, y = map(int, input().split())
        tempres = []
        for j in range(len(res)):
            for i1 in range(-d, d + 1):
                q = d - abs(i1)
                for j1 in range(-q, q + 1):
                    if abs(x - i1 - res[j][0]) + abs(y - j1 - res[j][1]) <= t:
                        if (x - i1, y - j1) not in tempres:
                            tempres.append((x - i1, y - j1))

        res = tempres

    print(len(res))
    for i in range(len(res)):
        print(res[i][0], res[i][1])



if __name__ == '__main__':
    start()
