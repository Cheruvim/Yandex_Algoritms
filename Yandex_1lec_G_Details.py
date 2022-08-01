def start():
    n, kDef, mDef = list(map(int, input().split()))
    m = 0
    if kDef < mDef:
        print(m)
        return

    while n >= kDef:
        kCount = n // kDef
        n -= kCount * kDef

        mCount = (kDef // mDef) * kCount
        m += mCount

        n += kCount * kDef - mCount * mDef

    print(m)

if __name__ == '__main__':
    start()