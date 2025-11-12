# fungsi + if else
def cek_angka(x):
    if x % 2 == 0:
        return "genap"
    else:
        return "ganjil"
    
hasil = cek_angka(7)
print("angka ini adalah:", hasil)

# latihan 1
def nilai_ujian(nilai):
    if nilai == 90:
        return "A"
    elif nilai == 80:
        return "B"
    elif nilai == 70:
        return "C"
    else:
        return "D, jangan meyerah, semangat lagi"
    
# minta input dari user
user_nilai = int(input("Masukan nilai ujian kamu: "))


hasil = nilai_ujian(user_nilai)
if hasil == "A":
    print("keren banget")
print("Nilai kamu:", hasil)

# latihan 2
def restoran(makanan):
    if makanan == "ayam goreng":
        return "silahkan ayam gorengnyanya"
    elif makanan == "kentang goreng":
        return "silahkan kentang gorengnnya"
    elif makanan == "nasi":
        return "silahkan ini nasinya"
    else:
        return "Masukan inputannya dulu"

print("halo selamat datang di restoran gojin rebel")
print("Menu : ayam goreng, kentang goreng, nasi")

user_customer = input("silakan mau pesan yang mana:")

jadi = restoran(user_customer)
print(jadi)