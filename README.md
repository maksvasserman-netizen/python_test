# python_test
from itertools import permutations

table = '12 14 16 21 23 24 25 32 35 41 42 46 52 53 61 64 67 74 75 76'
graf = 'АВ АГ АБ ВА ГА БА БГ ГБ БД ДБ ВГ ГВ ГД ДГ ДЕ ЕД ДК КД ВЕ ЕВ ЕК КЕ'

for per in permutations("АБВГДЕК"):
    new_table = table
    for i in range(1, 8):
        new_table = new_table.replace(str(i), per[i - 1])
    if set(new_table.split()) == set(graf.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
