# ===== NOMOR 2 =====
print("=== NOMOR 2 ===")  # Mencetak mundur kelipatan 3 dari 30 sampai 3
bilangan = 30
while bilangan >= 3:
    print("Kelipatan 3:", bilangan)
    bilangan -= 3

# ===== NOMOR 3 =====
print("=== NOMOR 3 ===")
angka = 1
ganjil = 0
genap = 0
while angka <= 10:
    if angka % 2 == 0:
        genap += 1
    else:
        ganjil += 1
    angka += 1
print("Jumlah Genap:", genap)
print("Jumlah Ganjil:", ganjil)
print("Jumlah Ganjil:", ganjil)

# ===== NOMOR 4 =====
print("=== NOMOR 4 ===")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# ===== NOMOR 5 =====
print("=== NOMOR 5 ===")
for i in range(5):
    print(i)

# ===== NOMOR 6 =====
print("=== NOMOR 6 ===")
for i in range(1, 6):
    print(2 ** i)

# ===== NOMOR 7 =====
print("=== NOMOR 7 ===")
for i in range(1, 11):
    if i == 3:
        continue
    if i == 8:
        break
    print("Angka:", i)

# ===== NOMOR 8 (diganti dengan isi 8.png) =====
print("=== NOMOR 8 ===")
total = 0
for angka in range(1, 101):
    total += angka
if total > 50:
    print(f"Total melebihi 50 saat menjumlah angka {angka}. Total: {total}")


# ===== NOMOR 9 =====
print("=== NOMOR 9 ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Bilangan ganjil:", i)
nrint("/\n")

# ===== NOMOR 10 =====
print("=== NOMOR 10 ===")
i = 1
while i <= 5:
    print("Nilai i:", i)
    i += 1
else:
    print("Perulangan while selesai tanpa break.")

# ===== NOMOR 11 =====
print("=== NOMOR 11 ===")
for i in range(1, 6):
    print("Nilai i:", i)
else:
    print("Perulangan for selesai tanpa break.")

# ===== NOMOR 12 =====
print("=== NOMOR 12 ===")
a = 10
b = 5
c = 0
print("(a > b) and (b > c):", (a > b) and (b > c))
print("(a < b) or (b > c):", (a < b) or (b > c))
print("not (a == b):", not (a == b))
print("\n")

# ===== NOMOR 13 =====
print("=== NOMOR 13 ===")
x = 5
y = 3
print("Logical AND (x and y):", x and y)
print("Logical OR (x or y):", x or y)
print("Bitwise AND (x & y):", x & y)
print("Bitwise OR (x | y):", x | y)
print("Bitwise XOR (x ^ y):", x ^ y)

# ===== NOMOR 14 =====
print("=== NOMOR 14 ===")
x = 4
geser_kiri = x << 2
geser_kanan = x >> 1
print(f"Nilai awal x: {x}")
print(f"x << 2: {geser_kiri}")
print(f"x >> 1: {geser_kanan}")

# ===== NOMOR 15 =====
print("=== NOMOR 15 ===")
x = 4
y = 1
a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2
print(a, b, c, d, e, f)