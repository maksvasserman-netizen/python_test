f = open('27-A (1).txt')

k = 0

for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[0] % 102 == 0:
        print(a)
    """if sum(a) == 360:
        k += 1
        print(k, a)"""