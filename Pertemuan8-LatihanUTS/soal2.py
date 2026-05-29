#Hapus duplikat tanpa set

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

hasil = []

for angka in data:
    if angka not in hasil:
        hasil.append(angka)

print(hasil)


