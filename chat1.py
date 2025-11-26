from random import random
import random

print("selamat datang di chat bot gojin rebel")
print("kata kunci:")
print("- siapa kamu")
print("- apa kabar")
print("- untuk apa kamu")

jawaban = {
    "siapa kamu" : ["aku adalah chat bot demo yang di buat gojin rebel untuk kamu!", ""],
    "apa kabar" : ["baik", "baik sekali", "agak badmood nih"],
    "untuk apa kamu" : ["untuk membantu mu dimana pun dan kapan pun!", "dibuat untuk mendampingimu"],
    "bye" : ["sampai jumpa trimakasih sudah menyobanya", "trimakasih sudah coba"],
}

def cari_jawaban(teks):
    max_ratio = 0
    respon = "aku belum tau maksudmu"
    for kunci, nilai in jawaban.items():
        ratio = fuzz.partial_ratio(teks, kunci)
        if ratio > max_ratio and ratio > 60:
            respon = random.choice(nilai)
            max_ratio = ratio 
        return respon

    while True:
        if teks == "bye":
            print("bot: bye! again")
            break
        print("bot:", cari_jawaban(teks))

# aku adalah chat bot demo yang di buat gojin rebel untuk kamu!
# untuk membantu mu dimana pun dan kapan pun!
# baik sekali, kalo kamu sendiri gimana nih harinya? 
