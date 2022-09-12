def start():
    t, d, n = map(int, input().split())
    arr = []

    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))

    curr = [0, 0, 0, 0]
    for i in arr:
        curr = [curr[0] - t, curr[1] + t, curr[2] - t, curr[3] + t]
        curr_temp = (i[0] + i[1] - d, i[0] + i[1] + d, i[0] - i[1] - d, i[0] - i[1] + d)
        curr = [max(curr[0], curr_temp[0]), min(curr[1], curr_temp[1]), max(curr[2], curr_temp[2]),
                min(curr[3], curr_temp[3])]

    points = []
    for xPlusY in range(curr[0], curr[1] + 1):
        for xMinusY in range(curr[2], curr[3] + 1):
            if (xPlusY + xMinusY) % 2 == 0:
                x = (xPlusY + xMinusY) // 2
                y = xPlusY - x
                points.append((x, y))

    print(len(points))
    for point in points:
        print(*point)


if __name__ == '__main__':
    start()
