def start():
    a1 = int(input())
    a2 = int(input())
    n1 = int(input())
    n2 = int(input())

    time1Min = n1 + (a1 * (n1 - 1))
    time1Max = n1 + (a1 * (n1 + 1))

    time2Min = n2 + (a2 * (n2 - 1))
    time2Max = n2 + (a2 * (n2 + 1))

    timeMin = max(time1Min, time2Min)
    timeMax = min(time1Max, time2Max)

    if timeMin > timeMax:
        print(-1)
        return

    print(str(timeMin) + " " + str(timeMax))

if __name__ == '__main__':
    start()
