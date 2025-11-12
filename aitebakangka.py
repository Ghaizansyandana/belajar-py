import random

print("selamat datang di game tebak angka")
print("pikiran satu angka dari 1 sampai 100 (jangan kasih tau aku ya).")

print("kalau sudah siap, tekan enter untuk mulai")

batas_bawah = 1
batas_atas = 100
percobaan = 0

while True:
    tebakan_ai = random.randint(batas_bawah, batas_atas)
    percobaan += 1
    print(f"\nAI menebak: {tebakan_ai}")

    jawaban = input("Apkah tebakanku terlalu (k)ecil, (b)esar, atau (b)enar?").lower()

    if jawaban == "b":
        print(f"Yess! aku berhasil menebak dalam{percobaan} kali percobaan.")
        break
    elif jawaban == "k":
        batas_bawah = tebakan_ai + 1
    elif jawaban == "b":
        batas_atas = tebakan_ai - 1
    else:
        print("jawaban nggak dikenal, coba ketik (k), (b), atau (b)enar.")    