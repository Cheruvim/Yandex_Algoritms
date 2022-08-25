def start():
    gen1 = input()
    gen2 = input()
    dic = {}
    count = 0

    for i in range(1, len(gen1)):
        temp = gen1[i-1] + gen1[i]
        if temp not in dic:
            dic[temp] = 1
        else:
            dic[temp] += 1

    for i in range(1, len(gen2)):
        temp = gen2[i - 1] + gen2[i]
        if temp in dic:
            if dic[temp] >= 1:
                count += dic[temp]
                dic[temp] = 0

    print(count)


if __name__ == '__main__':
    start()
