up_curr_line = 0
up_line = 0
down_curr_line = 0
down_line = 0
left_curr_line = 0
left_line = 0
right_curr_line = 0
right_line = 0


def start():
    global up_curr_line, up_line, down_curr_line, down_line, left_curr_line, left_line, right_curr_line, right_line

    t, d, n = map(int, input().split())
    arr = []

    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))

    left = (0, 0)
    right = (0, 0)
    up = (0, 0)
    down = (0, 0)

    for i in arr:
        left = (left[0] - t, left[1])
        right = (right[0] + t, right[1])
        up = (up[0], up[1] + t)
        down = (down[0], down[1] - t)

        left_curr = (i[0] - d, i[1])
        right_curr = (i[0] + d, i[1])
        up_curr = (i[0], i[1] + d)
        down_curr = (i[0], i[1] - d)
        up_temp = 0
        down_temp = 0
        right_temp = 0
        left_temp = 0

        up_curr_line = up_curr[1] + up_curr[0]
        up_line = up[1] + up[0]
        down_curr_line = down_curr[1] + down_curr[0]
        down_line = down[1] + down[0]
        left_curr_line = left_curr[0] - left_curr[1]
        left_line = left[0] - left[1]
        right_curr_line = right_curr[0] - right_curr[1]
        right_line = right[0] - right[1]

        if check_point(left_curr):
            left_temp = left_curr
        if check_point(left):
            left_temp = left

        if check_point(right_curr):
            right_temp = right_curr
        if check_point(right):
            right_temp = right

        if check_point(up_curr):
            up_temp = up_curr
        if check_point(up):
            up_temp = up

        if check_point(down_curr):
            down_temp = down_curr
        if check_point(down):
            down_temp = down

        if up_temp != 0:
            up = up_temp
        if down_temp != 0:
            down = down_temp
        if right_temp != 0:
            right = right_temp
        if left_curr != 0:
            left = left_temp

        if up_temp == 0 and down_temp == 0:
            temp = ((right[0] + right[1]) - (left[0] + left[1])) / 2
            down = (right[0] - temp, right[1] - temp)
            up = (left[0] + temp, left[1] + temp)

        if right_temp == 0 and left_temp == 0:
            temp = abs((up[0] + up[1]) - (down[0] + down[1])) / 2
            right = (down[0] + temp, down[1] + temp)
            left = (left[0] - temp, left[1] - temp)

        if right_temp != 0 and up_temp != 0 and left_temp == 0 and down_temp == 0:
            left = up
            down = right

        if right_temp != 0 and down_temp != 0 and left_temp == 0 and up_temp == 0:
            up = right
            left = down

        if left_temp != 0 and up_temp != 0 and right_temp == 0 and down_temp == 0:
            down = left
            right = up

        if left_temp != 0 and down_temp != 0 and right_temp == 0 and up_temp == 0:
            up = left
            right = down

    res = []
    up_line = up[1] + up[0]
    down_line = down[1] + down[0]
    left_line = left[0] - left[1]
    right_line = right[0] - right[1]

    for i in range(down[1], up[1] + 1):
        for j in range(abs(left_line - right_line) + 1):
            if check_in_box_for_current(left[0] + j, i):
                res.append((left[0] + j, i))

    print(len(res))
    print('\n'.join(' '.join(map(str, b)) for b in res))
    # for i in range(len(res)):
    #     print(res[i][0], res[i][1])


def check_point(x):
    if check_in_box_for_simple(x[0], x[1]) and check_in_box_for_current(x[0], x[1]):
        return True
    return False


def check_in_box_for_simple(x, y):
    if down_curr_line <= x + y <= up_curr_line and left_curr_line <= x - y <= right_curr_line:
        return True
    return False


def check_in_box_for_current(x, y):
    if down_line <= x + y <= up_line and left_line <= x - y <= right_line:
        return True
    return False


if __name__ == '__main__':
    start()
