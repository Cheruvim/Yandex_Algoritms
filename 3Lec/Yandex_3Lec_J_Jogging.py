def start():
    t, d, n = map(int, input().split())

    res = [(0, 0)]
    for i in range(n):
        x, y = map(int, input().split())
        temp = getPossiblePoints(x, y, d)
        tempres = []
        for j in range(len(res)):
            for k in range(len(temp)):
                if abs(temp[k][0] - res[j][0]) + abs(temp[k][1] - res[j][1]) <= t:
                    if temp[k] not in tempres:
                        tempres.append(temp[k])

        res = tempres

    print(len(res))
    for i in range(len(res)):
        print(res[i][0], res[i][1])


def getPossiblePoints(x, y, d):
    res = []

    for i in range(-d, d + 1):
        q = d - abs(i)
        for j in range(-q, q + 1):
            res.append((x - i, y - j))

    return res


if __name__ == '__main__':
    start()
