# latihan 1
 
nama = "gojin."
umur = 16
print(f"halo nama saya", nama, f"dan umurku", umur)

# latihan 2

umur = 17

if umur >= 17:
    print ("boleh bikin ktp")
else:
    print ("belum boleh bikin ktp")

# latihan 3

for i in range(1, 6):
    if i % 2 == 0:
        print (i, "bilangan ganjil")
    elif i % 2 == 1:
        print (i ,"bilangan genap")
    else:
        print ("not found")

# latihan 4

makanan = ["indomie", "ayam", "sate"]
print (len(makanan))

makanan.append("ikan")
print (makanan)

# latihan 5

n = 1
while n < 4:
    print("belajar python itu seru")
    n += 1

# latihan 6

nilai = 85

if nilai >= 90:
    print ("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai c")
else:
    print("perlu belajar lagi")

# latihan 7

total = 0

for total in range(1, 11):
    print (total)

# latihan 8

teman = ["gojin", "rebel", "rebelion"]

for nama in teman:
    print(f"halo", nama ,"apa kabar")

# latihan 9

rahasia = input("Masukan kata rahasia:")

if rahasia >= "main":
    print ("gaskenn")
else:
    print("salah")

# latihan 10

for i in range(5, 0, -1):
    print(i) 

print("Boom 💥")