def out_put_jiujiubiao(a, b):
    i = 1
    j = 1
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i >= j:
                print(j, '*', i, '=', i * j)


out_put_jiujiubiao(9, 9)
