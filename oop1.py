# contoh oop 

# struktur dasar class di python

class NamaClass:
    def __init__(self, atribut1, atribut2):
        self.atribut1 = atribut1
        self.atribut2 = atribut2

    def aksi(self):
        print("Aksi dari class ini")

# penjelasan singkat:
# class --> buat cetak (blueprint)
# __init__ --> fungsinya yang otomatis jalan pas object dibuat
# self --> ngarah ke object itu sendiri
# methon --> fungsi di dalam class

# contoh sederhananya :

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f"mobil {self.merk} berwarna {self.warna}")

# buat objectnya
mobil1 = Mobil("supra", "merah")
mobil2 = Mobil("civic", "hitan")

mobil1.info()
mobil2.info()

# latihan 1

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def info(self):
        print(f"{self.nama} bersuara {self.jenis}")

hewan1 = Hewan("kucing", "meong")
hewan2 = Hewan("anjing", "gokgok")

hewan1.info()
hewan2.info()

# latihan 2

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"halo, nama saya {self.nama} dan umur saya {self.umur}.")

    def ulang_tahun(self):
        self.umur += 1
        print(f"selamat ulang tahun {self.nama}! umur anda sekarang {self.umur}.")

orang1 = Manusia("gojin", 16)
orang1.perkenalan()
orang1.ulang_tahun()

# latihan 3

class Pelajar(Manusia):
    def __init__(self, nama, umur, sekolah):
        super().__init__(nama, umur)
        self.sekolah = sekolah

    def info_sekolah(self):
        print(f"{self.nama} sedang belajar di {self.sekolah}")

pelajar1 = Pelajar("gojin", 15, "smk")
pelajar1.info_sekolah()
