"""
Soal: Tentukan KPK dari 3 dan 4
------------------------------------------------------------------------------------------------------------------------
Algoritma:
------------------------------------------------------------------------------------------------------------------------
1.Membuat fungsi KPK(M,N)
    1.Deklarasi variabel o dengan nilai m
    2.Membuat perulangan selama variabel m modulus variabel n tidak sama dengan 0, maka:
        1.Deklarasi variabel m dengan nilai m + o
    3.Return m
2.Deklarasi variabel a dengan nilai 3
3.Deklarasi variabel b dengan nilai 4
4.Print KPK dari a dan b adalah KPK(a, b)

------------------------------------------------------------------------------------------------------------------------
Pseudocode:
------------------------------------------------------------------------------------------------------------------------
Function KPK(M, N):
    M ← O
    While M mod N != 0:
        M ← M + O
    Return M

A ← 3
B ← 4
PRINT "KPK dari A dan B adalah KPK(A, B)"

------------------------------------------------------------------------------------------------------------------------
"""


def kpk(m, n):
    o = m
    while m % n != 0:
        m += o
    return m


a = 3
b = 4
print('KPK dari ', a, 'dan ', b, 'adalah ', kpk(a, b))
