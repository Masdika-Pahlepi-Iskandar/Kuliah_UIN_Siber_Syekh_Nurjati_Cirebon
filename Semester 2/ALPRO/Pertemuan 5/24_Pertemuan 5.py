# 1. Comparison Operator
a = 20
b = 756
print(a > b)
print(a < b)
print(a == b)
print(a != b)

print("\n" + "="*50 + "\n")

# 2. Kuis 11
n = int(input("Masukkan angka n: "))
if n > 50:
    print(True)
else:
    print(False)

print("\n" + "="*50 + "\n")

# 3. Conditional statement: if tunggal
umur = int(input("Masukkan umur: "))
if umur >= 18:
    print("Boleh membuat KTP")
else:
    print("Belum boleh membuat KTP")

print("\n" + "="*50 + "\n")

# 4. Conditional statement: Rangkaian if
nilai = int(input("Masukkan nilai: "))
if nilai >= 85:
    print("Nilai A")
if nilai >= 70:
    print("Nilai B")
if nilai >= 60:
    print("Nilai C")
else:
    print("Nilai D")

print("\n" + "="*50 + "\n")

# 5. Conditional statement: if-else
nilai = int(input("Masukkan nilai: "))
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")

print("\n" + "="*50 + "\n")

# 6. Conditional statement: if-elif-else
nilai = int(input("Masukkan nilai: "))
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
else:
    print("Nilai D")

print("\n" + "="*50 + "\n")

# 7. Membandingkan 2 angka input
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if a > b:
    print("Angka pertama lebih besar")
elif a < b:
    print("Angka kedua lebih besar")
else:
    print("Kedua angka sama")

print("\n" + "="*50 + "\n")

# 8. Kuis 12
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a > b and a > c:
    print("Angka terbesar adalah:", a)
elif b > a and b > c:
    print("Angka terbesar adalah:", b)
else:
    print("Angka terbesar adalah:", c)

print("\n" + "="*50 + "\n")

# 9. Fungsi max()
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

paling_besar = max(a, b, c)
print("Angka paling besar adalah:", paling_besar)

print("\n" + "="*50 + "\n")

# 10. Kuis 13
pendapatan = int(input("Masukkan pendapatan: "))
pajak = 0
if pendapatan <= 50000000:
    pajak = pendapatan * 0.05
elif pendapatan <= 200000000:
    pajak = pendapatan * 0.15
elif pendapatan <= 400000000:
    pajak = pendapatan * 0.25
else:
    pajak = pendapatan * 0.30
print("Pajak yang harus dibayar adalah", pajak, "rupiah")