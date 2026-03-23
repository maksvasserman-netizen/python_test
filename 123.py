f = open('123.txt')
k = []
for s in f:
    a = [int(x) for x in s.split()]
    a2 = [int(x) **2 for x in s.split()]
    if a2[0] + a2[1] == a2[2]:
        k.append(a[0] + a[1])
    elif a2[0] + a2[2] == a2[1]:
        k.append(a[0] + a[2])
    elif a2[1] + a2[2] == a2[0]:
        k.append(a[1] + a[2])
print(max(k))
