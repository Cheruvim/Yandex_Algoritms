import re

def check_word(word):
    boo = False
    for i in word:
        if boo:
            return boo
        if 57 >= ord(i) >= 48:
            continue
        boo = True

    return boo


def get_rq(splited):
    count_special_word = int(splited[0])

    if splited[1] == "yes":
        rq_register = True
    else:
        rq_register = False

    if splited[2] == "yes":
        can_start_nums = True
    else:
        can_start_nums = False

    return count_special_word, rq_register, can_start_nums


def add_or_update(dic, word):
    if word not in dic:
        dic[word] = 0

    dic[word] += 1


def start():
    f = open("input.txt", "r")
    arr = f.readlines()

    splited = arr[0].split()
    count_special_word, rq_register, can_start_nums = get_rq(splited)
    line_num = 1
    spec_words = []
    for i in range(line_num, count_special_word + line_num):
        if not rq_register:
            spec_words.append(arr[i].strip().lower())
        else:
            spec_words.append(arr[i].strip())

    line_num = count_special_word + line_num
    dic = {}

    for i in range(line_num, len(arr)):
        temp_str = re.sub('\W+', ' ', arr[i]).strip().split()
        for j in range(len(temp_str)):
            if not rq_register:
                temp_str[j] = temp_str[j].lower()
            if not can_start_nums:
                if 57 >= ord(temp_str[j][0]) >= 48:
                    continue

            if temp_str[j] not in spec_words:
                if check_word(temp_str[j]):
                    add_or_update(dic, temp_str[j])

    word = ""
    max_count = 0
    for i in dic.keys():
        if dic[i] > max_count:
            word = i
            max_count = dic[i]

    print(word)


if __name__ == '__main__':
    start()
