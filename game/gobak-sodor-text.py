import random

# Fungsi untuk menampilkan papan permainan
def tampilkan_papan(papan):
    for baris in papan:
        print(" | ".join(baris))
        print("-" * (len(baris) * 4 - 1))

# Fungsi untuk memeriksa apakah pemain menang
def cek_menang(papan, pemain):
    # Cek baris
    for baris in papan:
        if all([cell == pemain for cell in baris]):
            return True
    # Cek kolom
    for kolom in range(3):
        if all([papan[baris][kolom] == pemain for baris in range(3)]):
            return True
    # Cek diagonal
    if all([papan[i][i] == pemain for i in range(3)]) or all([papan[i][2 - i] == pemain for i in range(3)]):
        return True
    return False

# Fungsi utama permainan
def main_galah_asin():
    # Inisialisasi papan 3x3
    papan = [[" " for _ in range(3)] for _ in range(3)]
    pemain_sekarang = "X"  # Pemain X mulai duluan
    langkah = 0

    print("Selamat datang di Galah Asin (Versi Sederhana)!")
    print("Pemain X dan O akan bergantian memilih kotak.")
    tampilkan_papan(papan)

    while True:
        # Input pemain
        try:
            baris, kolom = map(int, input(f"Pemain {pemain_sekarang}, pilih baris dan kolom (0-2): ").split())
            if papan[baris][kolom] != " ":
                print("Kotak sudah terisi, coba lagi!")
                continue
        except (ValueError, IndexError):
            print("Input tidak valid, masukkan angka 0-2 untuk baris dan kolom.")
            continue

        # Isi kotak
        papan[baris][kolom] = pemain_sekarang
        tampilkan_papan(papan)
        langkah += 1

        # Cek apakah ada pemenang
        if cek_menang(papan, pemain_sekarang):
            print(f"Selamat, Pemain {pemain_sekarang} menang!")
            break
        elif langkah == 9:  # Jika semua kotak terisi
            print("Permainan seri!")
            break

        # Ganti pemain
        pemain_sekarang = "O" if pemain_sekarang == "X" else "X"

# Jalankan permainan
if __name__ == "__main__":
    main_galah_asin()