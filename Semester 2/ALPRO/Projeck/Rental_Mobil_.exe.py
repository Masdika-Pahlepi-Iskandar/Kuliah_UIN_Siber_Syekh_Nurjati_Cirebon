# ==========================================
# SISTEM RENTAL MOBIL PAK SOKID GANTENG (VERSI GUI)
# Redesigned - Modern Dark Premium UI
# Siap di convert ke .EXE
# ==========================================
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import datetime

# ===============================
# LOGIN
# ===============================
USERNAME = "admin"
PASSWORD = "123"

# ===============================
# COLOR PALETTE - Deep Navy Gold Theme
# ===============================
C = {
    "bg_dark": "#0a0e1a",
    "bg_card": "#111827",
    "bg_input": "#1a2235",
    "bg_header": "#0d1520",
    "accent_gold": "#f0b429",
    "accent_blue": "#3b82f6",
    "accent_red": "#ef4444",
    "accent_green": "#10b981",
    "accent_orange": "#f97316",
    "text_white": "#f1f5f9",
    "text_muted": "#64748b",
    "text_gold": "#fbbf24",
    "border": "#1e2d45",
    "border_gold": "#f0b429",
    "row_even": "#111827",
    "row_odd": "#0f172a",
    "row_hover": "#1e3a5f",
    "selected": "#1d4ed8",
}

# ===============================
# DATA MOBIL
# ===============================
mobil = [
    {"nama": "Toyota Avanza", "harga": 300000, "status": "Tersedia"},
    {"nama": "Honda Brio", "harga": 250000, "status": "Tersedia"},
    {"nama": "Toyota Innova", "harga": 500000, "status": "Tersedia"},
    {"nama": "Mitsubishi Pajero", "harga": 800000, "status": "Tersedia"},
]

riwayat = []

# ===============================
# FORMAT RUPIAH
# ===============================
def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

# ===============================
# HELPER: CUSTOM MESSAGEBOX
# ===============================
def custom_popup(parent, judul, pesan, mode="info"):
    popup = tk.Toplevel(parent)
    popup.title(judul)
    popup.configure(bg=C["bg_card"])
    popup.resizable(False, False)
    popup.grab_set()

    w, h = 480, 320
    px = parent.winfo_x() + (parent.winfo_width() - w) // 2
    py = parent.winfo_y() + (parent.winfo_height() - h) // 2
    popup.geometry(f"{w}x{h}+{px}+{py}")

    icon_map = {
        "info": ("★", C["accent_gold"]),
        "error": ("✖", C["accent_red"]),
        "warning": ("⚠", C["accent_orange"]),
        "success": ("✔", C["accent_green"])
    }

    icon, ic = icon_map.get(mode, ("★", C["accent_gold"]))

    tk.Label(
        popup,
        text=icon,
        font=("Segoe UI", 28),
        bg=C["bg_card"],
        fg=ic
    ).pack(pady=(20, 4))

    tk.Label(
        popup,
        text=judul,
        font=("Segoe UI", 13, "bold"),
        bg=C["bg_card"],
        fg=C["text_white"]
    ).pack()

    frame_msg = tk.Frame(popup, bg=C["bg_input"], bd=0)
    frame_msg.pack(fill="both", expand=True, padx=20, pady=12)

    txt = tk.Text(
        frame_msg,
        bg=C["bg_input"],
        fg=C["text_white"],
        font=("Consolas", 9),
        bd=0,
        relief="flat",
        wrap="word",
        padx=12,
        pady=10
    )

    txt.insert("1.0", pesan.strip())
    txt.config(state="disabled")
    txt.pack(fill="both", expand=True)

    btn = tk.Button(
        popup,
        text=" OK ",
        font=("Segoe UI", 10, "bold"),
        bg=ic,
        fg="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=20,
        pady=6,
        command=popup.destroy
    )

    btn.pack(pady=(0, 18))
    popup.wait_window()

# ===============================
# LOGIN WINDOW
# ===============================
def buat_login():
    login_window = tk.Tk()
    login_window.title("Rental Mobil Pak Sokid Ganteng — Login")
    login_window.geometry("440x520")
    login_window.resizable(False, False)
    login_window.configure(bg=C["bg_dark"])

    # Center window
    login_window.update_idletasks()
    sw = login_window.winfo_screenwidth()
    sh = login_window.winfo_screenheight()
    x = (sw - 440) // 2
    y = (sh - 520) // 2
    login_window.geometry(f"440x520+{x}+{y}")

    # ---- Top accent bar ----
    accent_bar = tk.Frame(login_window, bg=C["accent_gold"], height=4)
    accent_bar.pack(fill="x", side="top")

    # ---- Logo / Brand ----
    tk.Label(
        login_window,
        text="🚗",
        font=("Segoe UI Emoji", 40),
        bg=C["bg_dark"],
        fg=C["accent_gold"]
    ).pack(pady=(40, 0))

    tk.Label(
        login_window,
        text="RENTAL MOBIL PAK SOKID GANTENG",
        font=("Segoe UI", 18, "bold"),
        bg=C["bg_dark"],
        fg=C["text_white"]
    ).pack()

    tk.Label(
        login_window,
        text="Panel Administrasi",
        font=("Segoe UI", 10),
        bg=C["bg_dark"],
        fg=C["text_muted"]
    ).pack(pady=(2, 30))

    # ---- Card Frame ----
    card = tk.Frame(login_window, bg=C["bg_card"], bd=0, relief="flat")
    card.pack(padx=40, fill="x")

    def make_field(parent, label_text, show=None):
        tk.Label(
            parent,
            text=label_text,
            font=("Segoe UI", 9, "bold"),
            bg=C["bg_card"],
            fg=C["text_muted"],
            anchor="w"
        ).pack(fill="x", padx=20, pady=(14, 2))

        frame_e = tk.Frame(parent, bg=C["border"], bd=0)
        frame_e.pack(fill="x", padx=20)

        inner = tk.Frame(frame_e, bg=C["border"])
        inner.pack(fill="x", padx=1, pady=1)

        entry = tk.Entry(
            inner,
            font=("Segoe UI", 11),
            bg=C["bg_input"],
            fg=C["text_white"],
            insertbackground=C["accent_gold"],
            relief="flat",
            bd=0,
            show=show
        )

        entry.pack(fill="x", ipady=8, padx=10)
        return entry

    entry_user = make_field(card, "USERNAME")
    entry_pass = make_field(card, "PASSWORD", show="●")

    tk.Frame(card, bg=C["bg_card"], height=20).pack()

    def do_login(event=None):
        user = entry_user.get()
        pw = entry_pass.get()

        if user == USERNAME and pw == PASSWORD:
            login_window.destroy()
            buka_aplikasi()
        else:
            entry_pass.delete(0, "end")
            entry_user.config(bg="#2d1515")
            entry_pass.config(bg="#2d1515")

            login_window.after(
                600,
                lambda: [
                    entry_user.config(bg=C["bg_input"]),
                    entry_pass.config(bg=C["bg_input"])
                ]
            )

            messagebox.showerror(
                "Login Gagal",
                "Username / Password Salah!",
                parent=login_window
            )

    btn_login = tk.Button(
        card,
        text="MASUK →",
        font=("Segoe UI", 11, "bold"),
        bg=C["accent_gold"],
        fg=C["bg_dark"],
        relief="flat",
        bd=0,
        cursor="hand2",
        pady=11,
        command=do_login
    )

    btn_login.pack(fill="x", padx=20, pady=(0, 24))

    entry_pass.bind("<Return>", do_login)
    entry_user.bind("<Return>", lambda e: entry_pass.focus())

    def on_hover_in(e):
        btn_login.config(bg="#fcd34d")

    def on_hover_out(e):
        btn_login.config(bg=C["accent_gold"])

    btn_login.bind("<Enter>", on_hover_in)
    btn_login.bind("<Leave>", on_hover_out)

    # ---- Footer ----
    tk.Label(
        login_window,
        text="© 2025 Rental Mobil Pak Sokid Ganteng. All rights reserved.",
        font=("Segoe UI", 8),
        bg=C["bg_dark"],
        fg=C["text_muted"]
    ).pack(side="bottom", pady=14)

    entry_user.focus()
    login_window.mainloop()

# ===============================
# JALANKAN
# ===============================
buat_login()