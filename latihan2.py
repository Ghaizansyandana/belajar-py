# latihan 1 daftar belanja
belanja = ["indomie", "nugget", "kornet", "oreo"]
print(belanja[1])
print(len(belanja))

belanja.append("ayam")
belanja.remove("oreo")

print(belanja)

# latihan 2 kontak sederhana
kontak = {"andi": "08948", "Budi": "08482" }
print(kontak["andi"])

kontak["cici"] = "092738"
print(kontak)

# latihan 3 kuadrat angka 
angka = [x for x in range (1, 6)]
print(angka)

kuadrat = [x**2 for x in angka]
print(kuadrat)