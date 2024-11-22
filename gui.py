import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from calc import Kalkulator
from PIL import Image, ImageTk

def hitung():
    bb = entry_bb.get()
    tb = entry_tb.get()
    usia = entry_usia.get()
    gender = var_gender.get()
    akt = combo_akt.get()

    # Mengecek input
    if not bb or not tb or not usia or not akt or akt == "Pilih":
        label_hasil.configure(text="Semua kolom harus diisi!", text_color="red")
        return

    try:
        bb = int(bb)
        tb = int(tb)
        usia = int(usia)
        akt = int(akt)
    except ValueError:
        label_hasil.configure(text="Masukkan angka yang valid!", text_color="red")
        return

    if akt < 1 or akt > 5:
        label_hasil.configure(text="Tingkat aktivitas harus antara 1 dan 5!", text_color="red")
        return

    # Perhitungan selanjutnya tetap sama
    kalkulator = Kalkulator(bb, tb, usia, gender, akt)
    kalori = kalkulator.bmr()
    protein = kalkulator.protein()
    lemak = kalkulator.lemak()
    karbo = kalkulator.karbo()
    gula = kalkulator.gula()

    # Menampilkan hasil pada label
    label_hasil.configure(
        text=(
            f"Energi: {kalori} kkal\n"
            f"Protein: {protein} gram\n"
            f"Lemak: {lemak} gram\n"
            f"Karbohidrat: {karbo} gram\n"
            f"Gula Maksimal: {gula} gram"
        ),
        text_color="white",
        
    )

# Tema
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green")

# Membuat window utama
window = ctk.CTk()
window.title("Kalkulator BMR")
window.geometry("500x600")

# Font
font = ctk.CTkFont(family="Comic Sans MS", size=14)

# logo di aplikasi
logo_image = ctk.CTkImage(light_image=Image.open("logo.png"), size=(100, 100))
label_logo = ctk.CTkLabel(window, image=logo_image, text="")
label_logo.pack(pady=10)

label_judul = ctk.CTkLabel(window, text="Kalkulator BMR", font=ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold"))
label_judul.pack(pady=5)

# Membuat frame untuk input
frame_input = ctk.CTkFrame(window, corner_radius=15)
frame_input.pack(pady=20, padx=20, fill="both")
frame_input.grid_columnconfigure(0, weight=1, uniform="equal")
frame_input.grid_columnconfigure(1, weight=1, uniform="equal")
frame_input.grid_columnconfigure(2, weight=1, uniform="equal")

# Input Tinggi Badan
label_tb = ctk.CTkLabel(frame_input, text="Tinggi Badan (cm):", font=font)
label_tb.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_tb = ctk.CTkEntry(frame_input, font=font)
entry_tb.grid(row=0, column=1, padx=10, pady=5)

# Input Berat Badan
label_bb = ctk.CTkLabel(frame_input, text="Berat Badan (kg):", font=font)
label_bb.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_bb = ctk.CTkEntry(frame_input, font=font)
entry_bb.grid(row=1, column=1, padx=10, pady=5)

# Input Usia
label_usia = ctk.CTkLabel(frame_input, text="Usia (tahun):", font=font)
label_usia.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_usia = ctk.CTkEntry(frame_input, font=font)
entry_usia.grid(row=2, column=1, padx=10, pady=5)

# Combobox tingkat aktivitas
label_akt = ctk.CTkLabel(frame_input, text="Tingkat Aktivitas:", font=font)
label_akt.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Pilih jenis kelamin
label_gender = ctk.CTkLabel(frame_input, text="Jenis Kelamin:", font=font)
label_gender.grid(row=4, column=0, padx=10, pady=5, sticky="w")
var_gender = ctk.StringVar(value="pria")  # Default ke "pria"
radio_pria = ctk.CTkRadioButton(frame_input, text="Pria", variable=var_gender, value="pria", font=font)
radio_pria.grid(row=4, column=1, padx=10, pady=5, sticky="w")
radio_wanita = ctk.CTkRadioButton(frame_input, text="Wanita", variable=var_gender, value="wanita", font=font)
radio_wanita.grid(row=4, column=2, padx=10, pady=5, sticky="w")

# Dropdown untuk memilih tingkat aktivitas
aktivitas_options = [1, 2, 3, 4, 5]  # Opsi dropdown
combo_akt = ttk.Combobox(frame_input, values=aktivitas_options, font=("Comic Sans MS", 10), state="readonly")
combo_akt.grid(row=3, column=1, padx=10, pady=5)
combo_akt.set("Pilih")  # Default value

# Tombol untuk menghitung
button_hitung = ctk.CTkButton(window, text="Hitung Kebutuhan Nutrisi", command=hitung, font=font)
button_hitung.pack(pady=10)

# Frame untuk menampilkan hasil
frame_hasil = ctk.CTkFrame(window, corner_radius=15, fg_color="#3A3A3A")
frame_hasil.pack(pady=20, padx=20, fill="both", expand=True)

# Label untuk menampilkan hasil
label_hasil = ctk.CTkLabel(
    frame_hasil,
    text="Hasil Perhitungan Akan Ditampilkan Di Sini",
    font=font,
    text_color="gray",
    wraplength=400,
)
label_hasil.pack(padx=10, pady=10)

window.mainloop()
