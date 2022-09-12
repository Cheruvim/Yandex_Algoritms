def start():
    n = int(input())
    dic = {}
    for i in range(n):
        first, second = map(str, input().split())
        dic[first] = second
        dic[second] = first

    ans = str(input())
    print(dic[ans])


if __name__ == '__main__':
    start()
