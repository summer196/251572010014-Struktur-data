#gunakan key value untuk mengetahui koordinat posisi nama mahasiswa

mahasiswa = {
    (1,1): 'Andi',
    (1,2): 'Budi',
    (2.1): 'Cici',
}

for posisi, nama in mahasiswa.items():
    print(f"posisi : {posisi} : {nama}")

print("Posisi (1,2) adalah :", {mahasiswa[(1,2)]})