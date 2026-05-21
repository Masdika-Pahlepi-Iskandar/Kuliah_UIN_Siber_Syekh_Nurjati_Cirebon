# ============================================
# 1. Membuat tuple dan tampilkan
# ============================================
print("=== 1. Membuat tuple dan tampilkan ===")
buah = ("apel", "mangga", "jeruk")
print(buah)

# ============================================
# 2. Menggunakan tuple (akses index)
# ============================================
print("\n=== 2. Menggunakan tuple (akses index) ===")
print("Elemen pertama:", buah[0])
print("Elemen terakhir:", buah[-1])
print("Elemen index 1 sampai akhir:", buah[1:])

# ============================================
# 3. Memodifikasi tuple (akan error karena immutable)
# ============================================
print("\n=== 3. Memodifikasi tuple (error) ===")
try:
    # Mencoba mengubah isi tuple - akan memunculkan TypeError
    buah[0] = "pisang"
except TypeError as e:
    print("Error:", e)
    print("Tuple bersifat immutable (tidak bisa diubah)")

# ============================================
# 4. Menggunakan tuple dengan len(), +, *, in, not in
# ============================================
print("\n=== 4. Operasi pada tuple ===")
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
print("len(tuple1):", len(tuple1))
print("tuple1 + tuple2:", tuple1 + tuple2)
print("tuple2 * 3:", tuple2 * 3)
print("Apakah 2 ada di tuple1?", 2 in tuple1)
print("Apakah 6 tidak ada di tuple1?", 6 not in tuple1)

# ============================================
# 5. Penugasan simultan pada tuple
# ============================================
print("\n=== 5. Penugasan simultan (tuple unpacking) ===")
data = ("Masdika", 20, "Informatika")
nama, umur, jurusan = data
print("Nama:", nama)
print("Umur:", umur)
print("Jurusan:", jurusan)

# Swap nilai tanpa variabel bantuan
a = 10
b = 20
print(f"Sebelum swap: a={a}, b={b}")
a, b = b, a
print(f"Setelah swap: a={a}, b={b}")

# ============================================
# 6. Membuat dictionary dan tampilkan
# ============================================
print("\n=== 6. Membuat dictionary ===")
mahasiswa = {
    "nama": "Masdika Pahlepi",
    "nim": "2530801014",
    "kelas": "2A Informatika"
}
print(mahasiswa)

# ============================================
# 7. Mengakses isi dictionary
# ============================================
print("\n=== 7. Mengakses isi dictionary ===")
print("Nama mahasiswa:", mahasiswa["nama"])
print("NIM:", mahasiswa["nim"])
# Akses dengan get() agar aman jika key tidak ada
print("Alamat (get):", mahasiswa.get("alamat", "Tidak tersedia"))

# ============================================
# 8. Method keys()
# ============================================
print("\n=== 8. Method keys() ===")
print("Keys dari dictionary:", mahasiswa.keys())

# ============================================
# 9. Method values()
# ============================================
print("\n=== 9. Method values() ===")
print("Values dari dictionary:", mahasiswa.values())

# ============================================
# 10. Method items()
# ============================================
print("\n=== 10. Method items() ===")
print("Items (key, value) pairs:", mahasiswa.items())

# Looping dengan items
for key, value in mahasiswa.items():
    print(f"{key} -> {value}")

# ============================================
# 11. Method update()
# ============================================
print("\n=== 11. Method update() ===")
mahasiswa.update({"alamat": "Jl. Raya No. 123", "angkatan": 2025})
print("Setelah update:", mahasiswa)

# ============================================
# 12. Method popitem()
# ============================================
print("\n=== 12. Method popitem() ===")
# popitem() menghapus item terakhir (sejak Python 3.7)
item_terhapus = mahasiswa.popitem()
print("Item yang dihapus:", item_terhapus)
print("Dictionary setelah popitem:", mahasiswa)

# ============================================
# 13. Modifikasi dictionary (langsung assign)
# ============================================
print("\n=== 13. Modifikasi dictionary (langsung assign) ===")
mahasiswa["kelas"] = "2A - Reguler"
mahasiswa["status"] = "Aktif"
print("Setelah modifikasi langsung:", mahasiswa)

# ============================================
# 14. Menangani exception (try-except)
# ============================================
print("\n=== 14. Menangani exception dengan try-except ===")
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print(f"10 / {angka} = {hasil}")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: Masukkan harus berupa angka!")

# ============================================
# 15. Menangani multiple exception
# ============================================
print("\n=== 15. Multiple exception ===")
try:
    data_list = [1, 2, 3]
    indeks = int(input("Masukkan index list (0-2): "))
    pembagi = int(input("Masukkan pembagi: "))
    hasil = data_list[indeks] / pembagi
    print(f"Hasil = {hasil}")
except IndexError:
    print("Error: Index di luar jangkauan list!")
except ZeroDivisionError:
    print("Error: Pembagi tidak boleh nol!")
except ValueError:
    print("Error: Input harus berupa bilangan bulat!")
except Exception as e:
    print(f"Terjadi error tak terduga: {e}")
else:
    print("Operasi berhasil tanpa error.")
finally:
    print("Blok finally selalu dijalankan.")

print("\n=== Selesai ===")