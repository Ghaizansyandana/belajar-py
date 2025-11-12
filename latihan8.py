class Laptop:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga

    def info(self):
        print(f"Laptop ini merknya {self.mek} dan harganya Rp.{self.harga}")

laptop1 = Laptop("HP", 1500000)
laptop1.info() 