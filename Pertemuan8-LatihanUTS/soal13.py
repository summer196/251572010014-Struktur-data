data = {'Andi':88, 'Budi':72, 'Cici':65, 'Deni':91, 'Eka':68, 'Fani':76}

grade = {'A': [], 'B': [], 'C': []}

for nama, nilai in data.items():
    if nilai >= 85:
        grade['A'].append(nama)
    elif nilai >= 70:
        grade['B'].append(nama)
    else:
        grade['C'].append(nama)

print("A:", grade['A'])
print("B:", grade['B'])
print("C:", grade['C'])