for m in range(2, 10):
    for n in range(2, m):
        if m % n == 0:
            print(m, '不是素数')
            break
    else:
        print(m, '是素数')
