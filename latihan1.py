# latihan 1 konversi

c = float(input("Masukan suhu (C):"))
f = (c * 9/5) + 32
print(f"{c}c = {f}f")

# latihan 2 faktorial

def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
        return hasil
    
n = int(input("Masukan angka:  "))
print(f"Faktorial dari {n} = {faktorial(n)}")

# latihan 3 palindrome

kata = input("Masukan kata: ").lower()
if kata == kata[::-1]:
    print("palindrome")
else:
    print("bukan palindrone")

