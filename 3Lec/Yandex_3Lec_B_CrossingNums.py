def start():
    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    nums = set(arr)
    nums2 = set(arr2)

    for i in nums:
        if i in nums2:
            print(i, end=" ")


if __name__ == '__main__':
    start()
