#algoritma mencari nilai maksimal

angka = [2,3,452,5,512,23,623,63]
max = angka[0]

for a in angka:
    if a > max:
        max = a

print("nilai maksimum", max)