def fun(a, b, *c):  # * is rest operator which uses rest of the values
    print(a)
    print(b)
    print(c)


fun(1, 2, 3, 4, 5, 6, 7)


d, e, f, *g = [10, 11, 12, 13, 14, 15, 16, 17]
print(g)


h, i, j, *k = (10, 11, 12, 13, 14, 15, 16, 17)
print(k)


l, m, n, *o = {10, 11, 12, 13, 14, 15, 16, 17}
print(o)

