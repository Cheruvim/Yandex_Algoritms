def append_or_update(dic, symbol, count):
    if symbol not in dic:
        dic[symbol] = 0

    dic[symbol] += count


def start():
    g, s = map(int, input().split())
    word = input()
    text = input()

    word_dir = {}
    for i in word:
        append_or_update(word_dir, i, 1)

    count = 0
    text_dir = {}
    for i in text[:len(word)]:
        if i in word_dir:
            append_or_update(text_dir, i, 1)

    eqCount = 0
    reqCount = len(word_dir.keys())

    for i in text_dir:
        if text_dir[i] == word_dir[i]:
            eqCount += 1

    if eqCount == reqCount:
        count += 1

    for i in range(len(word), len(text)):
        last_symbol = text[i-len(word)]
        if last_symbol in word_dir:
            if word_dir[last_symbol] == text_dir[last_symbol]:
                eqCount -= 1
            append_or_update(text_dir, last_symbol, -1)

        if text[i] in word_dir:
            if text[i] in text_dir:
                if word_dir[text[i]] == text_dir[text[i]] and text[i] != last_symbol:
                    eqCount -= 1

            append_or_update(text_dir, text[i], 1)
            if word_dir[text[i]] == text_dir[text[i]]:
                eqCount += 1
        if text[i] != last_symbol and last_symbol in word_dir:
            if word_dir[last_symbol] == text_dir[last_symbol]:
                eqCount += 1

        if eqCount == reqCount:
            count += 1

    print(count)


if __name__ == '__main__':
    start()
