#Mencari Nilai terkecil
angka = [34, 7, 23, 32, 5, 62]

terbesar = angka[0]
terkecil = angka[0]

for nilai in angka:
    if nilai > terbesar:
        terbesar = nilai
    if nilai < terkecil:
        terkecil = nilai

print("Terbesar:", terbesar)
print("Terkecil:", terkecil)
