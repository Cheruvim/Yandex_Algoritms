def start():
    rows, colums, count = list(map(int, input().split()))
    arr = [[0] * (colums+2) for i in range(rows+2)]
    mines = []
    for i in range(count):
        xMin, yMin = list(map(int, input().split()))
        mines.append((xMin, yMin))

    calc(arr, mines)

    for i in range(1, len(arr)-1):  # len(A) - возвращает количество строк в матрице А
        for j in range(1, len(arr[i])-1):  # len(A[i]) - возвращает количество элементов в строке i
            print(arr[i][j], end=' ')
        print()


def calc(arr, mines):
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]

    for xmin, ymin in mines:
        for i in range(8):
            arr[xmin + dx[i]][ymin + dy[i]] += 1

    for xmin, ymin in mines:
        arr[xmin][ymin] = "*"



if __name__ == '__main__':
    start()
