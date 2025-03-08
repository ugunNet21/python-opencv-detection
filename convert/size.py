from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, StringVar
from PIL import Image
import os

def compress_image(input_path, output_path, max_size_mb, quality=85, max_resolution=None):
    """
    Kompres gambar dengan mengubah kualitas dan resolusi.

    :param input_path: Path ke gambar asli
    :param output_path: Path untuk menyimpan gambar yang dikompres
    :param max_size_mb: Ukuran maksimal gambar dalam MB
    :param quality: Kualitas gambar (0-100), default 85
    :param max_resolution: Resolusi maksimal (lebar, tinggi), default None
    """
    if not os.path.exists(input_path):
        messagebox.showerror("Error", f"File {input_path} tidak ditemukan!")
        return

    with Image.open(input_path) as img:
        # Ubah resolusi jika diperlukan
        if max_resolution:
            img.thumbnail(max_resolution, Image.ANTIALIAS)

        # Simpan gambar dengan kualitas yang ditentukan
        img.save(output_path, quality=quality)

        # Periksa ukuran file
        while os.path.getsize(output_path) > max_size_mb * 1024 * 1024:
            quality -= 5
            if quality < 5:
                break
            img.save(output_path, quality=quality)

        messagebox.showinfo("Sukses", f"Gambar berhasil dikompres: {output_path}\n"
                                      f"Ukuran file: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")

def select_input_file():
    file_path = filedialog.askopenfilename(
        initialdir="/",  # Ganti dengan direktori default yang diinginkan
        title="Pilih Gambar",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")]
    )
    if file_path:
        input_path.set(file_path)  # Masukkan path yang dipilih ke Entry widget

def select_output_file():
    file_path = filedialog.asksaveasfilename(
        initialdir="/",  # Ganti dengan direktori default yang diinginkan
        title="Simpan Gambar",
        defaultextension=".jpg",
        filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")]
    )
    if file_path:
        output_path.set(file_path)  # Masukkan path yang dipilih ke Entry widget

def start_compression():
    input_file = input_path.get()
    output_file = output_path.get()
    max_size = max_size_entry.get()
    width = width_entry.get()
    height = height_entry.get()

    # Validasi input
    if not input_file or not output_file:
        messagebox.showerror("Error", "Harap pilih file input dan output!")
        return
    if not max_size:
        messagebox.showerror("Error", "Harap masukkan ukuran maksimal (MB)!")
        return

    try:
        max_size = float(max_size)
    except ValueError:
        messagebox.showerror("Error", "Ukuran maksimal harus berupa angka!")
        return

    # Jika resolusi diisi, pastikan valid
    resolution = None
    if width and height:
        try:
            resolution = (int(width), int(height))
        except ValueError:
            messagebox.showerror("Error", "Resolusi harus berupa angka!")
            return

    compress_image(input_file, output_file, max_size, quality=85, max_resolution=resolution)

# Buat GUI
root = Tk()
root.title("Image Compressor")

# Variabel untuk menyimpan path file
input_path = StringVar()
output_path = StringVar()

# Input file
Label(root, text="File Input:").grid(row=0, column=0, padx=5, pady=5)
Entry(root, textvariable=input_path, width=50).grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Pilih File", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Output file
Label(root, text="File Output:").grid(row=1, column=0, padx=5, pady=5)
Entry(root, textvariable=output_path, width=50).grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Pilih File", command=select_output_file).grid(row=1, column=2, padx=5, pady=5)

# Max size
Label(root, text="Ukuran Maksimal (MB):").grid(row=2, column=0, padx=5, pady=5)
max_size_entry = Entry(root, width=10)
max_size_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
max_size_entry.insert(0, "1")  # Default value

# Resolution
Label(root, text="Resolusi Maksimal (lebar x tinggi):").grid(row=3, column=0, padx=5, pady=5)
width_entry = Entry(root, width=10)
width_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
Label(root, text="x").grid(row=3, column=1, padx=80, pady=5, sticky="w")
height_entry = Entry(root, width=10)
height_entry.grid(row=3, column=1, padx=100, pady=5, sticky="w")

# Start button
Button(root, text="Kompres Gambar", command=start_compression).grid(row=4, column=1, padx=5, pady=10)

# Jalankan aplikasi
root.mainloop()