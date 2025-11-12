class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def info(self):
        print(f"{self.nama} - Rp{self.harga} (stok : {self.stok})")

class KeranjangBelanja:
    def __init__(self):
        self.item = []

    def tambah_produk(self, produk, jumlah):
        if produk.stok >= jumlah:
            produk.stok -= jumlah
            self.item.append((produk, jumlah))
            print(f"{produk.nama} x{jumlah} ditambahkan ke keranjang.")
        else:
            print(f"stok tidak cukup!")

    def total_harga(self):
        total = 0
        for produk, jumlah in self.item:
            total += produk.harga * jumlah
        return total
    
class Kasir:
    def __init__(self, nama):
        self.nama = nama

    def cetak_struk(self, keranjang):
        print(f"\nkasir: {self.nama}")
        print("==== STRUK PEMBELIAN ====")
        for produk, jumlah in keranjang.item:
            print(f"{produk.nama} x{jumlah} = Rp{produk.harga * jumlah}")
        print(f"total: Rp{keranjang.total_harga()}")
        print("=========================")

# -- simulasi ---
produk1 = Produk("kopi rebel", 15000, 10)
produk2 = Produk("indomie goreng", 5000, 20)

keranjang = KeranjangBelanja()
keranjang.tambah_produk(produk1, 2)
keranjang.tambah_produk(produk2, 3)

kasir = Kasir("gojin")
kasir.cetak_struk(keranjang)
