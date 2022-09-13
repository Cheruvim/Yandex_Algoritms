def start():
    f = open("input.txt", "r")
    arr = list(map(str, f.read().split("\n")))
    dic = {}
    for i in arr:
        temp = i.split()
        if len(temp) != 3:
            continue
        if temp[0] not in dic:
            dic[temp[0]] = {}

        if temp[1] not in dic[temp[0]]:
            dic[temp[0]][temp[1]] = 0

        dic[temp[0]][temp[1]] += int(temp[2])

    for i in sorted(dic.keys()):
        print(i + ":")
        for j in sorted(dic[i].keys()):
            print(j, dic[i][j])


if __name__ == '__main__':
    start()
