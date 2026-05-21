# ============================================
# 1. Variabel lokal (di dalam fungsi)
# ============================================
def contoh_lokal():
    x = 10          # variabel lokal, hanya ada di fungsi ini
    print("Nilai x di dalam fungsi:", x)

contoh_lokal()
# print(x)  # Error jika dijalankan, karena x tidak dikenal di luar fungsi

# ============================================
# 2. Variabel di luar fungsi - 1 (bisa diakses)
# ============================================
bilangan = 2   # variabel global

def perkalian_bilangan(y):
    return bilangan * y

print("Hasil perkalian (global):", perkalian_bilangan(5))  # 2*5 = 10

# ============================================
# 3. Variabel di luar fungsi - 2 (tertutup variabel lokal)
# ============================================
bilangan = 3   # global

def perkalian_bilangan_local(y):
    bilangan = 7   # lokal, mengalahkan global
    return bilangan * y

print("Hasil perkalian (lokal override):", perkalian_bilangan_local(5))  # 7*5 = 35

# ============================================
# 4. Keyword global (mengubah variabel global di dalam fungsi)
# ============================================
bilangan = 3

def ubah_global():
    global bilangan
    bilangan = 5

print("Sebelum ubah_global():", bilangan)
ubah_global()
print("Setelah ubah_global():", bilangan)

# ============================================
# 5. Kuis IMT (Indeks Massa Tubuh) dengan jenis kelamin
# ============================================
def hitung_imt(berat, tinggi):
    return berat / (tinggi ** 2)

jenis_kelamin = input("pilih jenis kelamin (L/P): ")
berat = float(input("Masukkan berat badan anda (kg): "))
tinggi = float(input("Masukkan tinggi badan anda (m): "))

imt = hitung_imt(berat, tinggi)

if jenis_kelamin == "L" or jenis_kelamin == "l":
    if imt < 18.5:
        kategori = "Kurus"
    elif 18.5 <= imt <= 25.0:
        kategori = "Normal"
    elif 25.0 < imt <= 27.0:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"
    print(f"Index massa tubuh anda tergolong {kategori}, dengan nilai IMT = {imt:.2f}")
else:
    print("Jenis kelamin anda tidak ada (hanya L/P)")

# ============================================
# 6. Fungsi segitiga - 1 (dengan tiga if terpisah)
# ============================================
def cek_segitiga1(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print("Segitiga (1,1,1):", cek_segitiga1(1,1,1))   # True
print("Segitiga (1,1,3):", cek_segitiga1(1,1,3))   # False

# ============================================
# 7. Fungsi segitiga - 2 (menggunakan OR)
# ============================================
def cek_segitiga2(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print("Segitiga (3,4,5):", cek_segitiga2(3,4,5))   # True
print("Segitiga (1,2,3):", cek_segitiga2(1,2,3))   # False

# ============================================
# 8. Fungsi segitiga - 3 (return langsung dengan and)
# ============================================
def cek_segitiga3(a, b, c):
    return a + b > c and b + c > a and c + a > b

print("Segitiga (2,2,2):", cek_segitiga3(2,2,2))   # True
print("Segitiga (1,1,2):", cek_segitiga3(1,1,2))   # False

# ============================================
# 9. Kuis faktorial (iteratif)
# ============================================
def faktorial(n):
    # bilangan yang akan di faktorial harus lebih besar dari 0
    if n < 0:
        return None
    # 0! dan 1! nilainya sama (1)
    if n < 2:
        return 1

    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

n = int(input("masukan nilai yang ingin di faktorial :"))
print(n, "! =", faktorial(n))

# ============================================
# 10. Kuis Fibonacci (iteratif)
# ============================================
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = 1
    elem_2 = 1
    hasil_jumlah = 0  # untuk menampung hasil penjumlahan

    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2
        elem_1 = elem_2
        elem_2 = hasil_jumlah

    return hasil_jumlah

# test
for n in range(1, 10):
    print(n, "->", fibonacci(n))

# ============================================
# 11. Rekursif faktorial
# ============================================
def faktorial_rekursif(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * faktorial_rekursif(n - 1)

print(f"\nFaktorial rekursif 5! = {faktorial_rekursif(5)}")
print(f"Faktorial rekursif 7! = {faktorial_rekursif(7)}")

# ============================================
# 12. Rekursif Fibonacci
# ============================================
def fibonacci_rekursif(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

print("\nDeret Fibonacci (rekursif):")
for i in range(1, 10):
    print(f"{i} -> {fibonacci_rekursif(i)}")