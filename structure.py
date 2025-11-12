# struktur data & kontrol lanjutan

angka = [1, 2, 3, 4, 5]
print(angka[0])     # akses index ke-0
print(len(angka))   # panjang list

angka.append(6)     # tambah item
angka.remove(3)     # hapus item
print(angka)

# tuple (immutable list)

data = (10, 20, 30)
print(data[1])
#  data[1] = 50 error, karna tuple tidak bisa di ubah

# set (unik, tidak bisa berurutan)

buah = {"apel", "pisang", "apel"}
print(buah) # otomatis hilang duplikat
buah.add("jeruk")
print(buah)

# dictionary (key-value)

murid = {"nama": "ghaizan", "umur": 16, "jurusan": "RPL"}
print(murid["nama"])
murid["umur"] = 17          # update value
murid["hobi"] = "coding"    # tambah key
print(murid)

# list comprehension

angka = [x for x in range (1, 6)]
print(angka)    # [1, 2, 3, 4, 5]

kuadrat = [x**2 for x in angka]
print(kuadrat)  # [1, 4, 9, 16, 25]

# exception handling

try:
    n = int(input("Masukan Angka :"))
    print(10 / n)
except ValueError:
    print("input harus angka")
except ZeroDivisionError:
    print("tidak bisa bagi 0")