def start():
    a1 = int(input())
    b1 = int(input())
    a2 = int(input())
    b2 = int(input())
    c1 = int(input())
    c2 = int(input())

    if a1 == 0 and a2 == 0 and b1 == 0 and b2 == 0 and c1 == 0 and c2 == 0:
        print("5")
        return

    if a1 == 0 and b1 == 0 and c1 != 0:
        print("0")
        return

    if a2 == 0 and b2 == 0 and c2 != 0:
        print("0")
        return

    if a1 == 0 and a2 == 0:
        res = (c1 - c2) / (b1 - b2)
        print(str(4) + " " + str(res))
        return

    if b1 == 0 and b2 == 0:

        res = (c1 - c2) / (a1 - a2)
        print(str(3) + " " + str(res))
        return

    if a1 == 0 and b2 == 0:
        y = c1 / (a1 + b1)
        x = c2 / (a2 + b2)
        print("2 " + str(x), str(y))
        return

    elif a2 == 0 and b1 == 0:
        x = c1 / (a1 + b1)
        y = c2 / (a2 + b2)
        print("2 " + str(x), str(y))
        return

    n = a1 / a2

    if a1 / n == a2 and b1 / n == b2 and c1 / n != c2:
        print(0)
        return

    if a1 / n == a2 and b1 / n == b2 and c1 / n == c2:
        print("1 " + str((a1 / b1) * (-1)) + " " + str(c1 / b1))
        return

    resY = (c1 - c2 * n) / (b1 - b2 * n)
    resX = (c1 - resY * b1) / a1

    print("2 " + str(resX) + " " + str(resY))




if __name__ == '__main__':
    start()


def start():
    a = float(input())


    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    if a * d == b * c and a * f != c * e:
        print(0)
    elif a == 0 and c == 0 and b * f != d * e:
        print(0)
    elif b == 0 and d == 0 and a * f != c * e:
        print(0)
    elif a * d == b * c and a * f == c * e:
        if b == 0 and d == 0:
            if a != 0 and c != 0:
                print(3, e / a)
            elif a == 0:
                if e == 0:
                    print(3, f / c)
            elif c == 0:
                if f == 0:
                    print(3, e / a)
        elif a == 0 and c == 0:
            if b != 0:
                print(4, e / b)
            elif d != 0:
                print(4, f / d)
        elif b != 0:
            print(1, -a / b, e / b)
        elif d != 0:
            print(1, -c / d, f / d)
    else:
        x = (e * d - b * f) / (a * d - b * c)
        y = (a * f - e * c) / (a * d - b * c)
        print(2, x, y)

if __name__ == '__main__':
    start()

