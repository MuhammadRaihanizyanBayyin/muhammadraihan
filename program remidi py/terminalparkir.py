# Program Menghitung Tarif Parkir Kendaraan
# Penulis: ChatGPT
# Deskripsi: Program ini digunakan untuk menghitung tarif parkir sesuai durasi parkir kendaraan

# Fungsi utama untuk menghitung tarif parkir
def hitung_tarif_parkir(durasi_jam):
    """
    Fungsi ini menerima input durasi parkir (dalam jam) dan menghitung tarif parkir berdasarkan:
    - Rp3.000 untuk 2 jam pertama
    - Rp1.500 per jam tambahan setelah 2 jam
    - Tambahan biaya Rp10.000 jika parkir lebih dari 24 jam
    """
    TARIF_2_JAM_PERTAMA = 3000  # Tarif untuk 2 jam pertama
    TARIF_PER_JAM_TAMBAHAN = 1500  # Tarif per jam tambahan setelah 2 jam
    BIAYA_TAMBAHAN_24_JAM = 10000  # Biaya tambahan jika melebihi 24 jam

    # Inisialisasi tarif awal
    total_tarif = 0

    # Logika perhitungan tarif
    if durasi_jam <= 2:
        total_tarif = TARIF_2_JAM_PERTAMA  # Jika parkir <= 2 jam
    else:
        # Tarif 2 jam pertama
        total_tarif = TARIF_2_JAM_PERTAMA
        # Tarif tambahan untuk jam setelah 2 jam pertama
        jam_tambahan = durasi_jam - 2
        total_tarif += jam_tambahan * TARIF_PER_JAM_TAMBAHAN

    # Tambahkan biaya tambahan jika melebihi 24 jam
    if durasi_jam > 24:
        total_tarif += BIAYA_TAMBAHAN_24_JAM

    return total_tarif


# Fungsi untuk meminta input durasi parkir dari pengguna
def input_durasi():
    """
    Fungsi untuk meminta input durasi parkir dari pengguna
    Memastikan input berupa angka positif
    """
    while True:
        try:
            durasi = float(input("Masukkan durasi parkir kendaraan (dalam jam): "))
            if durasi <= 0:
                print("Durasi harus lebih dari 0. Silakan coba lagi.")
            else:
                return durasi
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")


# Fungsi utama untuk menjalankan program
def main():
    """
    Fungsi utama program yang memadukan input pengguna dan perhitungan tarif
    """
    print("\n=== Program Perhitungan Tarif Parkir ===")
    print("Ketentuan Tarif Parkir:")
    print("- Rp3.000 untuk 2 jam pertama")
    print("- Rp1.500 per jam tambahan setelah 2 jam")
    print("- Tambahan Rp10.000 jika parkir lebih dari 24 jam\n")

    # Input durasi parkir
    durasi = input_durasi()

    # Hitung tarif berdasarkan durasi
    total_tarif = hitung_tarif_parkir(durasi)

    # Tampilkan hasil
    print(f"Tarif parkir untuk {durasi:.1f} jam adalah: Rp{total_tarif:,}")


# Menjalankan program jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
