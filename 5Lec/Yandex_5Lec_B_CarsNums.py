def start():
    n1, s = map(int, input().split())
    arr = list(map(int, input().split()))

    last = 0
    sum_arr = []
    for i in range(n1):
        sum_arr.append(last)
        last += arr[i]

    sum_arr.append(last)

    last_num = 0
    sum = 0
    res = 0
    for i in range(n1):
        while last_num < len(arr) and sum < s:
            sum = sum_arr[last_num + 1] - sum_arr[i]
            last_num += 1
            if sum == s:
                res += 1
                break

        last_num -= 1

        sum = 0

    print(res)


if __name__ == '__main__':
    start()
