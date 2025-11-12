# fungsi
def halo_user(nama):
    print("Halo", nama, "apa kabar?")

halo_user("Gojin")

# latihan 1
def tambah(a, b):
    hasil = a + b
    print("Hasil penjumlahan:", hasil)

tambah(1, 2)

# latihan 2
def cek_genap(angka):
    if angka % 2 == 0:
        print(angka, "adalah bilangan genap")
    else:
        print(angka, "adalah bilangan ganjil")

cek_genap(7)
cek_genap(10)

# return

def tambah(a, b):
    return a + b

hasil = tambah(5,3)
print("hasilnya adalah", hasil)

# latihan 3
def kali(a, b):
    return a * b

hasil = kali(10,2)
print("hasilnya adalah", hasil)