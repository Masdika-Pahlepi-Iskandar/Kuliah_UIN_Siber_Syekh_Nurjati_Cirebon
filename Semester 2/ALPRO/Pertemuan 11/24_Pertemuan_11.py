# ==========================================
# RETURNING A RESULT FROM A FUNCTION
# Masdika Pahlepi I.
# ==========================================


# soal 1
print("--output soal 1--")

def selamat_ulang_tahun(harapan=True):
    print("Tiga...")
    print("Dua...")
    print("Satu...")

    if not harapan:
        return

    print("Selamat Ulang Tahun")

selamat_ulang_tahun()


# soal 2
print("\n--output soal 2--")

def selamat_ulang_tahun(harapan=True):
    print("Tiga...")
    print("Dua...")
    print("Satu...")

    if not harapan:
        return

    print("Selamat Ulang Tahun")

selamat_ulang_tahun(False)


# soal 3
print("\n--output soal 3--")

def fungsi_malas():
    return 123

x = fungsi_malas()

print("Hasil dari fungsi malas adalah", x)


# soal 4
print("\n--output soal 4--")

def fungsi_malas():
    print("aku lagi mode malas")
    return 123

print("Mata kuliah ini seru banget!")
fungsi_malas()
print("Mata kuliah ini boring banget..")


# soal 5
print("\n--output soal 5--")

def fungsi_aneh(n):
    if (n % 2 == 0):
        return True

print(fungsi_aneh(12))
print(fungsi_aneh(13))


# soal 6
print("\n--output soal 6--")

def penjumlahan_list(lst):
    s = 0

    for elemen in lst:
        s += elemen

    return s

print(penjumlahan_list([10, 13, 15]))


# soal 7
print("\n--output soal 7--")

def penjumlahan_list(lst):
    s = 0

    for elemen in lst:
        s += elemen

    return s

print(penjumlahan_list(7))


# soal 8
print("\n--output soal 8--")

def fungsi_list_aneh(n):
    list_aneh = []

    for i in range(0, n):
        list_aneh.insert(0, i)

    return list_aneh

print(fungsi_list_aneh(5))


# soal 9
print("\n--output soal 9--")

def tahun_kabisat(tahun):
    if tahun % 4 != 0:
        return False
    elif tahun % 100 != 0:
        return True
    elif tahun % 400 != 0:
        return False
    else:
        return True


# data uji
data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

# testing
for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "-> ", end="")

    hasil = tahun_kabisat(th)

    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")


# soal 10
print("\n--output soal 10--")

def tahun_kabisat(tahun):
    if tahun % 4 != 0:
        return False
    elif tahun % 100 != 0:
        return True
    elif tahun % 400 != 0:
        return False
    else:
        return True


def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28


# data uji
data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

# testing
for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "-> ", end="")

    hasil = tahun_kabisat(th)

    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")


# soal 11
print("\n--output soal 11--")

def tahun_kabisat(tahun):
    if tahun % 4 != 0:
        return False
    elif tahun % 100 != 0:
        return True
    elif tahun % 400 != 0:
        return False
    else:
        return True


def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28


def hari_pada_tahun(tahun, bulan, hari):

    # Validasi bulan
    if bulan < 1 or bulan > 12:
        return None

    # Validasi hari
    if hari < 1 or hari > hari_didalam_bulan(tahun, bulan):
        return None

    total_hari = 0

    # Jumlahkan semua hari dari bulan sebelumnya
    for b in range(1, bulan):
        total_hari += hari_didalam_bulan(tahun, b)

    # Tambahkan hari di bulan sekarang
    total_hari += hari

    return total_hari


print(hari_pada_tahun(2000, 12, 31))
print(hari_pada_tahun(2001, 12, 31))
print(hari_pada_tahun(2000, 1, 1))
print(hari_pada_tahun(2000, 2, 29))
print(hari_pada_tahun(2000, 13, 1))
print(hari_pada_tahun(2000, 2, 30))


# soal 12
print("\n--output soal 12--")

def cek_prima(bilangan):
    if bilangan <= 1:
        return False

    for i in range(2, int(bilangan ** 0.5) + 1):
        if bilangan % i == 0:
            return False

    return True


for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")

print()


# soal 13
print("\n--output soal 13--")

def cek_prima(bilangan):
    if bilangan <= 1:
        return False

    for i in range(2, int(bilangan ** 0.5) + 1):
        if bilangan % i == 0:
            return False

    return True


for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")

print()


# soal 14
print("\n--output soal 14--")

def Liter100km_ke_mpg(liter):
    mil = 100 * 1000 / 1609.344
    galon = liter / 3.785411784

    return mil / galon


def mpg_ke_Liter100km(mil):
    km100 = mil * 1609.344 / 1000
    liter = 1 * 3.785411784

    return liter / km100


print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))

print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))