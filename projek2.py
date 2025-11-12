from datetime import datetime

def showroom(mobil):
    option = {
        "mercy": 9000000,
        "bmw": 8000000
    }
    if mobil in option:
        return option[mobil]
    else:
        return None
    
print("----- SELAMAT DATANG DI SHOWROOM MOBIL BANDUNG -----")
print("Car:")
print("- Mercy : 9000000")
print("- BMW : 8000000")
print("Ketik 'selesai kalau sudah selesai membeli.\n")

total = 0
pesanan_list = []

while True:
    pesanan = input("Mau Beli Mobil Apa Nih:").lower()
    if pesanan == "selesai":
        break

    harga = showroom(pesanan)
    if harga:
        print(f"{pesanan} Ditambahkan, Dengan Harga Rp{harga}")
        total += harga
        pesanan_list.append((pesanan, harga))
    else:
        print("Mobil Tidak Tersedia.")

# Diskon !0% kalau Total Di atas 300.000.000
diskon = 0
if total >= 3000000:
    diskon = total * 0.1
    print("\n Anda Dapat Diskon 10%!")

total_akhir = total - diskon 

# Minta Uang Pembayaran
print("\nStruk Pembelian mobil di Showroom Bandung")
for item, harga in pesanan_list:
    print(f"- {item} : Rp{harga}")

print("-----------------------------------------")
print(f"Subtotal : Rp{total}")
if diskon > 0:
    print(f"Diskon      : Rp{int(diskon)}")
print(f"Total      : Rp{int(total_akhir)}")

uang = int(input("\nMasukan Uang Pembayaran: Rp"))
kembalian = uang - total_akhir

if kembalian < 0:
    print("Uang Kurang, Silahkan Tambahkan Lagi.")
else:
    print(f"Kembalian Anda: Rp{int(kembalian)}")
    print("----- TERIMAKASIH TELAH MEMBELI MOBIL DISINI! SEMOGA SEHAT SELALU -----")

    # Simpan Struk Ke File
    waktu = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nama_file = f"struk_showroom_bandung_{waktu}.txt"

    with open(nama_file, "w") as file:
        file.write("------ STRUK SHOWROOM BANDUNG\n ------\n")
        file.write("---------------------------------------\n")
        for item, harga in pesanan_list:
            file.write(f"- {item} : Rp{harga}\n")
        file.write(f"---------------------------------------\n")
        file.write(f"Subtotal : Rp{total}\n")
        if diskon > 0:
            file.write(f"Diskon     : Rp{int(diskon)}\n")
            file.write(f"Total     : Rp{int(total_akhir)}\n")
            file.write(f"Uang     : Rp{int(uang)}\n")
            file.write(f"---------------------------------------\n")
            file.write(f"Terimakasih Banyak Sudah Mampir!\n")

        print(f"\n Struk Berhasil Disimpan Sebagai '{nama_file}'")     