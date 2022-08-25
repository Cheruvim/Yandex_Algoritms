def start():
    f = open("input.txt", "r")
    arr = list(map(str, f.read().split()))

    nums = set(arr)

    print(len(nums))


if __name__ == '__main__':
    start()
