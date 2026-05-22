# 1. Membuat fungsi input kemudian tampilkan ke konsol
nama = input("Masukkan nama Anda: ")
print("Halo", nama)

# 2. Membuat fungsi input dengan argumen
umur = input("Masukkan umur Anda: ")
print("Umur Anda adalah", umur)

# 3. Memahami hasil dari fungsi input
angka = input("Masukkan angka: ")
print(angka * 2)

# 4. Mengkonversi tipe data 1: Membuat konversi tipe data float pada fungsi input
bilangan = float(input("Masukkan bilangan desimal: "))
print("Hasil kali 2 =", bilangan * 2)

# 5. Mengkonversi tipe data 2: Membuat program untuk menghitung sisi miring segitiga
# dengan variable hypo untuk menampung hasil rumus pitagoras
a = float(input("Masukkan sisi a: "))
b = float(input("Masukkan sisi b: "))
hypo = (a**2 + b**2) ** 0.5
print("Sisi miring =", hypo)

# 6. Mengkonversi tipe data 2: Membuat program untuk menghitung sisi miring segitiga
# tanpa membuat variable untuk menampung hasil operasi
a = float(input("Masukkan sisi a: "))
b = float(input("Masukkan sisi b: "))
print("Sisi miring =", (a**2 + b**2) ** 0.5)

# 7. Operator Konkatenasi
depan = "Hello"
belakang = "World"
print(depan + " " + belakang)

# 8. Operator Replikasi
teks = "Python "
print(teks * 3)

# 9. Mengkonversi Tipe data 3: konversi ke string
umur = 20
print("Umur saya " + str(umur))

# 10. Melihat tipe data dari suatu variable
x = 10
print(type(x))

# 11. Kuis 7
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print("Selamat kamu sudah pintar matematika")

# 12. Kuis 8
x = float(input("Masukkan nilai x: "))

y = (2 * x) + (3 * x**2) - 1.0
print(y)

# 13. Kuis 9
jam = int(input("Jam mulai: "))
menit = int(input("Menit mulai: "))

durasi = int(input("Durasi (menit): "))

total_menit = menit + durasi
jam_selesai = jam + total_menit // 60
menit_selesai = total_menit % 60

print("Acara selesai pukul", jam_selesai, ":", menit_selesai)