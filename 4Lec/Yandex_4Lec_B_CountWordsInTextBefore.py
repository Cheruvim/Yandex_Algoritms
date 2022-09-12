def start():
    f = open("input.txt", "r")
    arr = list(map(str, f.read().split()))
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 0

        print(dic[i], end=" ")
        dic[i] += 1

if __name__ == '__main__':
    start()
