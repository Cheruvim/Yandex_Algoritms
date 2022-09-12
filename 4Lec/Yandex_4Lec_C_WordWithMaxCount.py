def start():
    f = open("input.txt", "r")
    arr = list(map(str, f.read().split()))
    maxCount = 0
    minWord = "t"
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1

        if dic[i] > maxCount:
            maxCount = dic[i]
            minWord = i

    for i in dic:
        if dic[i] == maxCount and i < minWord:
            minWord = i

    print(minWord)


if __name__ == '__main__':
    start()
