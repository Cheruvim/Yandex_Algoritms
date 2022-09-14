def check_word(dic, word):
    ex = False
    if word.lower() in dic:
        for i in range(len(word)):
            if ord(word[i]) <= 90:
                if i in dic[word.lower()]:
                    if ex:
                        return 1
                    ex = True
                else:
                    return 1
    else:
        for j in range(len(word)):
            if ord(word[j]) <= 90:
                if ex:
                    return 1
                ex = True

    if not ex:
        return 1

    return 0


def start():
    n = int(input())
    dic = {}
    for i in range(n):
        temp = input()
        if temp.lower() not in dic:
            dic[temp.lower()] = []
        for j in range(len(temp)):
            if ord(temp[j]) <= 90:
                dic[temp.lower()].append(j)
                break

    text = list(map(str, input().split()))
    errors = 0
    for i in text:
        errors += check_word(dic, i)

    print(errors)


if __name__ == '__main__':
    start()
