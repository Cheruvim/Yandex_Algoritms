def start():
    x1, y1, x2, y2 = list(map(int, input().split()))

    s1 = (x1 + x2) * max(y1, y2)
    s2 = max(x1, x2) * (y1 + y2)
    s3 = (x1 + y2) * max(x2, y1)
    s4 = max(x1, y2) * (x2 + y1)

    smin = min(s1, s2, s3, s4)
    if s1 == smin:
        print(str(x1 + x2) + " " + str(max(y1, y2)))
        return
    if s2 == smin:
        print(str(max(x1, x2)) + " " + str(y1 + y2))
        return
    if s3 == smin:
        print(str((x1 + y2)) + " " + str(max(x2, y1)))
        return
    if s4 == smin:
        print(str(max(x1, y2)) + " " + str((x2 + y1)))
        return

if __name__ == '__main__':
    start()
