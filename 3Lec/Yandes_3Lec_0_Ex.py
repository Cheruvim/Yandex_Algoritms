def start():
    dic = list(map(str, input().split()))
    text = list(map(str, input().split()))
    goodwords = set(dic)
    for word in dic:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])

    ans = []
    for word in text:
        ans.append(word in goodwords)

    print(ans)

if __name__ == '__main__':
    start()
