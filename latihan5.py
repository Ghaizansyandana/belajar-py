# latihan 1

def sapaan(nama):
    print("Halo", nama, "Selamat belajar python.")

sapaan("Gojin")

# latihan 2

def cek_angka(angka):
    if angka % 2 == 0:
        print(angka, "angka genap")
    else:
        print(angka, "angka ganjil")

cek_angka(1)
cek_angka(3)

# latihan 3

def restoran(makanan):
    menu = {
        "indomie goreng": 5000,
        "indomie kuah": 4000
    }
    return menu.get(makanan)

print(f"selamat datang di warkop rebel")
print(f"untuk hari ini ada diskon 1%")
print(f"menu:")
print(f"- indomie goreng: 5000")
print(f"- indomie kuah: 4000")
print(f"ketik selesai kalau sudah memesan")

total = 0 
pesanan_list = []

while True:
    pesanan = input("Mau pesan apa nih:").lower().strip()
    if pesanan == "selesai":
        break

    harga = restoran(pesanan)
    if harga is not None:
        print(f"{pesanan} ditambahkan, harga Rp{harga}")
        total += harga
        pesanan_list.append((pesanan, harga))
    else:
        print("menu gaada")

diskon = 0
if total >= 1000:
    diskon = total * 0.01
    print("\n kamu dapet diskon 1%")

total_akhir = total - diskon

print("-----------------------")
print(f"Subtotal : Rp{int(total)}")
if diskon > 0:
    print(f"Diskon  : Rp{int(diskon)}")
print(f"total   : Rp{int(total_akhir)}")

uang = int(input("\nmasukan uang pembayaran:"))
kembalian = uang - total_akhir

if kembalian < 0:
    print("uang kurang, silahkan tambah lagi")
else:
    print(f"kembalian kamu: Rp{int(kembalian)}")
    print("trimakasih sudah mampir di warkop gojin rebel, jangan kapok kalo kesini ya!")

# latihan 4

for i in range(5):
    print("Belajar python itu seru")