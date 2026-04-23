import threading

saldo = 10000000
def tarik(nama, jumlah):
    global saldo
    if saldo >= jumlah:
        saldo = saldo - jumlah
        print(nama, "BERHASIL")
    else:
        print(nama, "GAGAL")

t1 = threading.Thread(
    target = tarik, args=('andi', 7000000))
t2 = threading.Thread(
    target = tarik, args=('budi', 5000000))

t1.start(); t2.join()
t1.join(); t2.join()

print(saldo)