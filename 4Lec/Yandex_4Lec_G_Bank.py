dic = {}


def start():
    global dic
    f = open("input.txt", "r")
    arr = list(map(str, f.read().split("\n")))
    for i in arr:
        temp = i.split()
        if len(temp) < 1:
            continue

        if temp[0] == "DEPOSIT":
            DEPOSIT(temp)
        elif temp[0] == "TRANSFER":
            TRANSFER(temp)
        elif temp[0] == "INCOME":
            INCOME(temp)
        elif temp[0] == "BALANCE":
            BALANCE(temp)
        elif temp[0] == "WITHDRAW":
            WITHDRAW(temp)


def DEPOSIT(arr):
    if arr[1] not in dic:
        dic[arr[1]] = 0
    dic[arr[1]] += int(arr[2])


def INCOME(arr):
    for i in dic.keys():
        if dic[i] > 0:
            dic[i] = (dic[i] * (100 + int(arr[1])) / 100) // 1
            dic[i] = int(dic[i])


def BALANCE(arr):
    if arr[1] not in dic:
        print("ERROR")
    else:
        print(dic[arr[1]])


def TRANSFER(arr):
    if arr[1] not in dic:
        dic[arr[1]] = 0
    if arr[2] not in dic:
        dic[arr[2]] = 0

    dic[arr[1]] -= int(arr[3])
    dic[arr[2]] += int(arr[3])


def WITHDRAW(arr):
    if arr[1] not in dic:
        dic[arr[1]] = 0
    dic[arr[1]] -= int(arr[2])


if __name__ == '__main__':
    start()
