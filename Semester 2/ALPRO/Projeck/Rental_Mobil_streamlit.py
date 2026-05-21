import streamlit as st

# DATA
if "mobil" not in st.session_state:
    st.session_state.mobil = [
        {"nama": "Avanza", "harga": 300000, "status": "Tersedia"},
        {"nama": "Brio", "harga": 250000, "status": "Tersedia"},
        {"nama": "Innova", "harga": 500000, "status": "Tersedia"},
        {"nama": "Pajero", "harga": 800000, "status": "Tersedia"}
    ]

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

if "login" not in st.session_state:
    st.session_state.login = False

# LOGIN
st.title("🚗 Sistem Rental Mobil")

if not st.session_state.login:
    st.subheader("Login Admin")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pw == "123":
            st.session_state.login = True
            st.success("Login berhasil!")
        else:
            st.error("Login gagal!")

else:
    menu = st.sidebar.selectbox("Menu", [
        "Lihat Mobil", "Sewa Mobil", "Kembalikan Mobil", "Riwayat"
    ])

    # LIHAT MOBIL
    if menu == "Lihat Mobil":
        st.subheader("Daftar Mobil")
        for i, m in enumerate(st.session_state.mobil):
            st.write(f"**{i+1}. {m['nama']}**")
            st.write(f"Harga: {m['harga']}")
            st.write(f"Status: {m['status']}")
            st.divider()

    # SEWA MOBIL
    elif menu == "Sewa Mobil":
        st.subheader("Sewa Mobil")

        nama = st.text_input("Nama Penyewa")
        pilihan = st.selectbox(
            "Pilih Mobil",
            range(len(st.session_state.mobil)),
            format_func=lambda x: st.session_state.mobil[x]["nama"]
        )
        lama = st.number_input("Lama Sewa (hari)", min_value=1, step=1)

        if st.button("Sewa"):
            mobil = st.session_state.mobil[pilihan]

            if mobil["status"] == "Tersedia":
                harga = mobil["harga"]
                total = harga * lama

                # DISKON
                if lama >= 3:
                    diskon = total * 0.1
                    total -= diskon
                else:
                    diskon = 0

                mobil["status"] = "Disewa"

                transaksi = {
                    "nama": nama,
                    "mobil": mobil["nama"],
                    "lama": lama,
                    "total": total
                }

                st.session_state.riwayat.append(transaksi)

                st.success("Berhasil disewa!")
                st.write("### Struk")
                st.write("Nama:", nama)
                st.write("Mobil:", mobil["nama"])
                st.write("Lama:", lama, "hari")
                st.write("Diskon:", int(diskon))
                st.write("Total:", int(total))

            else:
                st.error("Mobil sedang disewa!")

    # KEMBALIKAN
    elif menu == "Kembalikan Mobil":
        st.subheader("Kembalikan Mobil")

        pilihan = st.selectbox(
            "Pilih Mobil",
            range(len(st.session_state.mobil)),
            format_func=lambda x: st.session_state.mobil[x]["nama"]
        )

        if st.button("Kembalikan"):
            mobil = st.session_state.mobil[pilihan]

            if mobil["status"] == "Disewa":
                mobil["status"] = "Tersedia"
                st.success("Mobil berhasil dikembalikan!")
            else:
                st.warning("Mobil belum disewa!")

    # RIWAYAT
    elif menu == "Riwayat":
        st.subheader("Riwayat Transaksi")

        if len(st.session_state.riwayat) == 0:
            st.info("Belum ada transaksi!")
        else:
            for r in st.session_state.riwayat:
                st.write("Nama:", r["nama"])
                st.write("Mobil:", r["mobil"])
                st.write("Lama:", r["lama"], "hari")
                st.write("Total:", int(r["total"]))
                st.divider()