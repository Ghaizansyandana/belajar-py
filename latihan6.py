class Karakter:
    def __init__(self, nama, darah, serangan):
        self.nama = nama
        self.darah = darah
        self.serangan = serangan

    def info(self):
        print(f"{self.nama} punya darah {self.darah} dan juga serangan {self.serangan}")

    def serang(self, target):
        if self.darah <= 0:
            print(f"{self.nama} sudah kalah dan tidak bisa menyerang")
            return

        print(f"{self.nama} serang {target.nama}!")
        target.darah -= self.serangan

        if target.darah <= 0:
            print(f"{target.nama} kalah!")
        else:
            (f"darah {target.nama} sekarang {target.darah}")

gojin = Karakter("gojin", 100, 20)
rebel = Karakter("rebel", 80, 25)

gojin.info()
rebel.info()

gojin.serang(rebel)
rebel.info()    



