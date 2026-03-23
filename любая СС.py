from string import ascii_lowercase

alf = '0123456789' + ascii_lowercase
m = ''
def per(n, o):
    s = ''
    while n > 0:
        ost = n % o
        s = alf[ost] + s
        n = n // o
    return s
n = int(input())
N = per(n, 3)
if int(N) % 3 != 0:
    N = '1' + str(N) + '02'
else:
    ost = (int(n) % 3) * 4


    def PER(b, O):
        s = ''
        while b > 0:
            ost = n % O
            s = alf[ost] + s
            b = b // O
        return s
    m = PER(ost, 3)
N = str(N) + str(m)
print(int(N, 3))
