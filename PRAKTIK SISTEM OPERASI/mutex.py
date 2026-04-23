import threading

saldo = 1000000
lock = threading.Lock()

def tarik_aman(nama, jumlah):
    global saldo
    lock.acquire()
    try:
        if saldo >= jumlah:
            saldo = saldo - jumlah
            print(nama, "Berhasil")
        else:
            print(nama, "Gagal")
    finally:
        lock.release()

t1 = threading.Thread(
    target = tarik_aman, args=('andi', 7000000))
t2 = threading.Thread(
    target = tarik_aman, args=('budi', 5000000))

t1.start(); t2.join()
t1.join(); t2.join()

print(saldo)