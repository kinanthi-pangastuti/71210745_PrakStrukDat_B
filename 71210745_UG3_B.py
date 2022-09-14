# Kinanthi P (71210745)
# UG3 - Program Pencarian Bil Faktorial

import math
n = int(input("Masukkan range data :"))
data = {}

for i in range(n):
    if (i%2==0):
        kunci = i
        nilai = math.factorial(i)
        data[kunci] = nilai
    else:
        continue
print(data)

keyyy = data.keys()
target = int(input("Data ditampilkan :"))

for x in keyyy:
    if (x==target):
        y = str(data.get(x))
        print("Data ditemukan: "+y)
        break

else:
    print("Data tidak ditemukan")
