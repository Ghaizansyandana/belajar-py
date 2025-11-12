import random

print("🎯 Selamat datang di game Tebak Angka Ajaib!")
print("Aku sudah memilih angka antara 1 sampai 20.")

angka_rahasia = random.randint(1, 20)
percobaan = 0

while True:
    tebakan = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    # Kondisi benar
    if tebakan == angka_rahasia:
        print(f"🔥 Keren! Kamu menebak dengan benar dalam {percobaan} kali percobaan.")
        break

    # Cek perbedaan jauh banget
    elif abs(tebakan - angka_rahasia) > 5:
        print("😅 Jauh banget! Coba lebih deket lagi!")

    # Cek lebih kecil / besar tapi masih dekat
    elif tebakan < angka_rahasia:
        print("🔼 Terlalu kecil! Naikin dikit.")
    else:
        print("🔽 Terlalu besar! Turunin dikit.")
