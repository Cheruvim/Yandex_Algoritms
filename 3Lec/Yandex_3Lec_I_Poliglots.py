def start():
    n = int(input())
    dic = {}

    for i in range(n):
        num = int(input())
        for i in range(num):
            lang = input()
            if lang not in dic:
                dic[lang] = 1
            else:
                dic[lang] += 1

    langs = []
    keys = dic.keys()
    for i in keys:
        if dic[i] == n:
            langs.append(i)

    print(len(langs))
    for i in langs:
        print(i)

    print(len(keys))
    for i in keys:
        print(i)


if __name__ == '__main__':
    start()
