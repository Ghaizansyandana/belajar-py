from datetime import datetime

def restoran(makanan):
    menu = {
        "ayam goreng": 15000,
        "kentang goreng": 10000,
        "nasi": 8000
    }
    if makanan in menu:
        return menu[makanan]
    else:
        return None


print("🍽️ Selamat datang di Restoran Gojin Rebel!")
print("Menu:")
print("- Ayam goreng : Rp15000")
print("- Kentang goreng : Rp10000")
print("- Nasi : Rp8000")
print("Ketik 'selesai' kalau sudah selesai pesan.\n")

total = 0
pesanan_list = []

while True:
    pesanan = input("Mau pesan apa: ").lower()
    if pesanan == "selesai":
        break

    harga = restoran(pesanan)
    if harga:
        print(f"✅ {pesanan} ditambahkan, harga Rp{harga}")
        total += harga
        pesanan_list.append((pesanan, harga))
    else:
        print("⚠️ Menu tidak tersedia, coba lagi ya.")

# Diskon 10% kalau total di atas 30.000
diskon = 0
if total >= 30000:
    diskon = total * 0.1
    print("\n🎉 Kamu dapet diskon 10%!")

total_akhir = total - diskon

# Minta uang pembayaran
print("\n🧾 Struk Pembelian Restoran Gojin Rebel")
for item, harga in pesanan_list:
    print(f"- {item} : Rp{harga}")

print("----------------------------")
print(f"Subtotal : Rp{total}")
if diskon > 0:
    print(f"Diskon   : Rp{int(diskon)}")
print(f"Total    : Rp{int(total_akhir)}")

uang = int(input("\nMasukkan uang pembayaran: Rp"))
kembalian = uang - total_akhir

if kembalian < 0:
    print("⚠️ Uangnya kurang, silakan tambahkan lagi.")
else:
    print(f"💰 Kembalian kamu: Rp{int(kembalian)}")
    print("Terima kasih sudah mampir di Restoran Gojin Rebel 😎")

    # Simpan struk ke file
    waktu = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nama_file = f"struk_gojin_rebel_{waktu}.txt"

    with open(nama_file,"w") as file:
        file.write("Struk Pembelian Restoran Gojin Rebel\n")
        file.write("------------------------------------\n")
        for item, harga in pesanan_list:
            file.write(f"- {item} : Rp{harga}\n")
        file.write(f"-------------------------\n")
        file.write(f"Subtotal : Rp{total}\n")
        if diskon > 0:
            file.write(f"Diskon     : Rp{int(diskon)}\n")
        file.write(f"Total     : Rp{int(total_akhir)}\n")
        file.write(f"Uang     : Rp{int(uang)}\n")
        file.write(f"-------------------------\n")
        file.write(f"Trima kasih Sudah Mampir \n")

        print(f"\n Struk berhasil disimpan sebagai '{nama_file}'")

