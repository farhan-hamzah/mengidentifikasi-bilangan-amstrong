import math
N = int(input())
akhir = 0
negatif = N < 0
N = abs(N)
while N > 0:
    hasil = N%10
    akhir = akhir*10 + hasil
    N = math.floor(N/10)
if negatif:
    akhir = -akhir
print(akhir)
