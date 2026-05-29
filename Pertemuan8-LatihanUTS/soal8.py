angka = [1, 2, 3, 4, 6, 8, 9]
target = 10

kiri = 0
kanan = len(angka) - 1

print("Pasangan yang jumlahnya 10:")
while kiri < kanan:
    total = angka[kiri] + angka[kanan]
    if total == target:
        print(f"({angka[kiri]}, {angka[kanan]})")
        kiri += 1
        kanan -= 1
    elif total < target:
        kiri += 1
    else:
        kanan -= 1