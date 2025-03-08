import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk membuat database dan tabel
def create_database():
    conn = sqlite3.connect('apotek.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS obat (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama TEXT NOT NULL,
                    stok INTEGER NOT NULL,
                    harga REAL NOT NULL)''')
    conn.commit()
    conn.close()

# Fungsi untuk menambah obat
def tambah_obat():
    nama = entry_nama.get()
    stok = entry_stok.get()
    harga = entry_harga.get()

    if nama and stok and harga:
        conn = sqlite3.connect('apotek.db')
        c = conn.cursor()
        c.execute("INSERT INTO obat (nama, stok, harga) VALUES (?, ?, ?)", (nama, stok, harga))
        conn.commit()
        conn.close()
        entry_nama.delete(0, tk.END)
        entry_stok.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Obat berhasil ditambahkan")
    else:
        messagebox.showwarning("Peringatan", "Semua field harus diisi")

# Fungsi untuk menampilkan stok obat
def tampilkan_stok():
    conn = sqlite3.connect('apotek.db')
    c = conn.cursor()
    c.execute("SELECT * FROM obat")
    rows = c.fetchall()
    conn.close()

    listbox_stok.delete(0, tk.END)
    for row in rows:
        listbox_stok.insert(tk.END, f"ID: {row[0]}, Nama: {row[1]}, Stok: {row[2]}, Harga: {row[3]}")

# Membuat GUI
app = tk.Tk()
app.title("Aplikasi Apotek")

# Label dan Entry untuk menambah obat
tk.Label(app, text="Nama Obat").grid(row=0, column=0)
entry_nama = tk.Entry(app)
entry_nama.grid(row=0, column=1)

tk.Label(app, text="Stok").grid(row=1, column=0)
entry_stok = tk.Entry(app)
entry_stok.grid(row=1, column=1)

tk.Label(app, text="Harga").grid(row=2, column=0)
entry_harga = tk.Entry(app)
entry_harga.grid(row=2, column=1)

# Tombol untuk menambah obat
tk.Button(app, text="Tambah Obat", command=tambah_obat).grid(row=3, column=0, columnspan=2)

# Listbox untuk menampilkan stok obat
listbox_stok = tk.Listbox(app, width=50)
listbox_stok.grid(row=4, column=0, columnspan=2)

# Tombol untuk menampilkan stok obat
tk.Button(app, text="Tampilkan Stok", command=tampilkan_stok).grid(row=5, column=0, columnspan=2)

# Membuat database saat aplikasi pertama kali dijalankan
create_database()

# Menjalankan aplikasi
app.mainloop()