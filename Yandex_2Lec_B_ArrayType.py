def start():
    arr = []
    temp = 0
    while temp != -2000000000:
        temp = int(input())
        if temp != -2000000000:
            arr.append(temp)

    CONSTANT = True
    ASCENDING = True
    WEAKLYASCENDING = True
    DESCENDING = True
    WEAKLYDESCENDING = True
    RANDOM = True

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            ASCENDING = False
            DESCENDING = False

        if arr[i] > arr[i - 1]:
            CONSTANT = False
            DESCENDING = False
            WEAKLYDESCENDING = False

        if arr[i] < arr[i - 1]:
            CONSTANT = False
            ASCENDING = False
            WEAKLYASCENDING = False

    if CONSTANT:
        print("CONSTANT")
    elif ASCENDING:
        print("ASCENDING")
    elif WEAKLYASCENDING:
        print("WEAKLY ASCENDING")
    elif DESCENDING:
        print("DESCENDING")
    elif WEAKLYDESCENDING:
        print("WEAKLY DESCENDING")
    elif RANDOM:
        print("RANDOM")

if __name__ == '__main__':
    start()
