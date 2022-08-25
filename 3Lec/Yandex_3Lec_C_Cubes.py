def start():
    # ann, boris = list(map(int, input().split()))
    # a = set()
    # b = set()
    # for i in range(ann):
    #     a.add(int(input()))
    # for i in range(boris):
    #     b.add(int(input()))
    #
    # print(len(a.intersection(b)))
    # print(*sorted(a.intersection(b)))
    # print(len(a.difference(b)))
    # print(*sorted(a.difference(b)))
    # print(len(b.difference(a)))
    # print(*sorted(b.difference(a)))

    n, m = map(int, input().split())
    arr1 = set()
    arr2 = set()
    arrCross = set()
    arrNotCross1 = set()
    arrNotCross2 = set()
    for i in range(n):
        arr1.add(int(input()))

    for i in range(m):
        arr2.add(int(input()))

    for i in arr1:
        if i in arr2:
            arrCross.add(i)

    for i in arr1:
        if i not in arrCross:
            arrNotCross1.add(i)

    for i in arr2:
        if i not in arrCross:
            arrNotCross2.add(i)

    print(len(arrCross))
    print(' '.join(str(n) for n in sorted(arrCross)))

    print(len(arrNotCross1))
    print(' '.join(str(n) for n in sorted(arrNotCross1)))

    print(len(arrNotCross2))
    print(' '.join(str(n) for n in sorted(arrNotCross2)))


if __name__ == '__main__':
    start()
