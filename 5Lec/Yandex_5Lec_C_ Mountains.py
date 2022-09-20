def start():
    n1 = int(input())
    arr = []
    for i in range(n1):
        _, temp = map(int, input().split())
        arr.append(temp)

    n2 = int(input())
    arr1 = []
    for i in range(n2):
        temp1, temp2 = map(int, input().split())
        arr1.append((temp1, temp2))

    sum_left_to_right = []
    last = arr[0]
    sum = 0
    for i in range(n1):
        sum_left_to_right.append(sum)
        if arr[i] >= last:
            sum += arr[i] - last
        last = arr[i]
    sum_left_to_right.append(sum)

    sum_right_to_left = []
    last = arr[n1 - 1]
    sum = 0
    for i in range(n1 - 1, -1, -1):
        sum_right_to_left.append(sum)
        if arr[i] >= last:
            sum += arr[i] - last
        last = arr[i]
    sum_right_to_left.append(sum)

    res = []
    for i in range(n2):
        if arr1[i][0] < arr1[i][1]:
            res.append(sum_left_to_right[arr1[i][1]] - sum_left_to_right[arr1[i][0]])
        elif arr1[i][0] > arr1[i][1]:
            res.append(sum_right_to_left[len(arr) - arr1[i][1] + 1] - sum_right_to_left[len(arr) - arr1[i][0] + 1])
        else:
            res.append(0)

    for i in range(n2):
        print(res[i])

if __name__ == '__main__':
    start()
