from fuzzywuzzy import fuzz
import random

# kumpulan respons chatbot
jawaban = {
    "halo" : ["Hai juga!", "Halo gimana kabarnya?", "Yo, Ada apa nihh?"],
    "apa kabar" : ["Baik banget! Gimana kabar kamu?", "Lagi semangat belajar nih!", "alhamdullilah baik!"],
    "siapa kamu" : ["Aku chatbot buatan gojin", "aku asisten virtual mu yang setia menemanimu dengan cinta"],
    "bye" : ["sampai jumpa!", "dadah jangan lupa belajar lagi besok ya", "bye love youuu"],
}

def cari_jawaban(teks):
    max_ratio = 0
    respon = "Aku belum paham maksudmu"
    for kunci, nilai in jawaban.items():
        ratio = fuzz.partial_ratio(teks, kunci)
        if ratio > max_ratio and ratio > 60:
            respon = random.choice(nilai)
            max_ratio = ratio
        return respon
    
    while True:
        if teks == "bye":
            print("Bot: Bye love youu")
            break
        print("Bot:", cari_jawaban(teks))
