# LOGIN
username_admin = "admin"
password_admin = "123"

# DATA
mobil = [
    {"nama": "Avanza", "harga": 300000, "status": "Tersedia"},
    {"nama": "Brio", "harga": 250000, "status": "Tersedia"},
    {"nama": "Innova", "harga": 500000, "status": "Tersedia"},
    {"nama": "Pajero", "harga": 800000, "status": "Tersedia"}
]

riwayat = []

# GARIS
def line():
    print("=" * 45)

# LOGIN
def login():
    print("=== LOGIN ADMIN ===")
    user = input("Username: ")
    pw = input("Password: ")

    if user == username_admin and pw == password_admin:
        print("Login berhasil!\n")
        return True
    else:
        print("Login gagal!\n")
        return False

# TAMPIL MOBIL
def tampil_mobil():
    print("\n=== DAFTAR MOBIL ===")
    for i, m in enumerate(mobil):
        line()
        print(f"{i+1}. {m['nama']}")
        print("Harga  :", m["harga"])
        print("Status :", m["status"])
    line()

# SEWA MOBIL
def sewa_mobil():
    tampil_mobil()
    pilih = int(input("Pilih mobil: "))
    nama = input("Nama penyewa: ")
    lama = int(input("Lama sewa (hari): "))

    if mobil[pilih-1]["status"] == "Tersedia":
        harga = mobil[pilih-1]["harga"]
        total = harga * lama

        # DISKON
        if lama >= 3:
            diskon = total * 0.1
            total -= diskon
        else:
            diskon = 0

        mobil[pilih-1]["status"] = "Disewa"

        transaksi = {
            "nama": nama,
            "mobil": mobil[pilih-1]["nama"],
            "lama": lama,
            "total": total
        }

        riwayat.append(transaksi)

        line()
        print("=== STRUK PEMBAYARAN ===")
        print("Nama   :", nama)
        print("Mobil  :", mobil[pilih-1]["nama"])
        print("Lama   :", lama, "hari")
        print("Diskon :", int(diskon))
        print("Total  :", int(total))
        line()

    else:
        print("Mobil sedang disewa!")

# KEMBALIKAN MOBIL
def kembalikan_mobil():
    tampil_mobil()
    pilih = int(input("Pilih mobil yang dikembalikan: "))

    if mobil[pilih-1]["status"] == "Disewa":
        mobil[pilih-1]["status"] = "Tersedia"
        print("Mobil berhasil dikembalikan!")
    else:
        print("Mobil memang belum disewa!")

# RIWAYAT
def tampil_riwayat():
    if len(riwayat) == 0:
        print("Belum ada transaksi!")
        return

    print("\n=== RIWAYAT TRANSAKSI ===")
    for r in riwayat:
        line()
        print("Nama  :", r["nama"])
        print("Mobil :", r["mobil"])
        print("Lama  :", r["lama"], "hari")
        print("Total :", int(r["total"]))
    line()

# MAIN
if login():
    while True:
        line()
        print("SISTEM RENTAL MOBIL PRO")
        line()
        print("1. Lihat Mobil")
        print("2. Sewa Mobil")
        print("3. Kembalikan Mobil")
        print("4. Riwayat")
        print("5. Keluar")

        pilih = int(input("Pilih: "))

        if pilih == 1:
            tampil_mobil()
        elif pilih == 2:
            sewa_mobil()
        elif pilih == 3:
            kembalikan_mobil()
        elif pilih == 4:
            tampil_riwayat()
        elif pilih == 5:
            print("Terima kasih!")
            break
        else:
            print("Pilihan salah!")