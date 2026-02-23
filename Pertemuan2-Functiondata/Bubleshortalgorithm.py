#Algoritma bubble sort (pengurutan)

angka = [5,7,8,5,2,1]

for i in range(len(angka)):
    for j in range(len(angka)-i-1):
        if angka[j] > angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]

print("hasil sorting", angka)