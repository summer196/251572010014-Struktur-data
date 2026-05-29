#Simulasi Printer
from collections import deque

antrian = deque(['Laporan', "Foto", 'Tugas'])
print("Antrian", list(antrian))

while antrian:
    job = antrian.popleft()
    print("Cetak : {job:<10} | Sisa :", list(antrian))
