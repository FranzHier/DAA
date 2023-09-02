"""
Soal: Menukar nilai pada dua variabel
------------------------------------------------------------------------------------------------------------------------
Algoritma:
------------------------------------------------------------------------------------------------------------------------
1.Deklarasi variabel P1 dengan nilai "Manggis"
2.Deklarasi variabel P2 dengan nilai "Pisang"
3.Deklarasi variabel P3 dengan nilai kosong ""
5.Print variabel P1, P2, P3
6.Deklarasi variabel P3 dengan nilai P1
7.Deklarasi variabel P1 dengan nilai P2
8.Deklarasi variabel P2 dengan nilai P3
9.Deklarasi variabel P3 dengan nilai kosong ""
10.Print variabel P1, P2, P3

------------------------------------------------------------------------------------------------------------------------
Pseudocode:
------------------------------------------------------------------------------------------------------------------------
P1 ← "Manggis"
P2 ← "Pisang"
P3 ← ""

PRINT "P1 P2 P3"
P3 ← P1
P1 ← P2
P2 ← P3
P3 ← ""
PRINT "P1 P2 P3"

------------------------------------------------------------------------------------------------------------------------
"""
P1 = "Manggis"
P2 = "Pisang"
P3 = ""

print('piring 1: ', P1, '\npiring 2: ', P2, '\npiring 3: ', P3)

P3 = P1
P1 = P2
P2 = P3
P3 = ""

print('\npiring 1: ', P1, '\npiring 2: ', P2, '\npiring 3: ', P3)
