def hitung_biaya_parkir(jenis_kendaraan, total_jam):
    """
    Fungsi untuk menghitung biaya parkir berdasarkan jenis kendaraan dan durasi parkir.

    Parameter:
    jenis_kendaraan (str): Jenis kendaraan, 'motor' atau 'mobil'.
    total_jam (int): Total waktu parkir dalam jam.

    Return:
    total_biaya (int): Total biaya parkir yang harus dibayar.
    """
    # Biaya dasar
    biaya_awal = 3000  # Biaya untuk 2 jam pertama
    biaya_motor_per_jam = 1000  # Biaya tambahan per jam untuk motor
    biaya_mobil_per_jam = 1500  # Biaya tambahan per jam untuk mobil
    biaya_tambahan_24_jam = 10000  # Biaya tambahan jika melebihi 24 jam

    # Hitung biaya parkir awal
    total_biaya = biaya_awal

    # Cek apakah parkir lebih dari 2 jam
    if total_jam > 2:
        kelebihan_jam = total_jam - 2  # Menghitung sisa jam setelah 2 jam pertama
        if jenis_kendaraan == "motor":
            total_biaya += kelebihan_jam * biaya_motor_per_jam
        elif jenis_kendaraan == "mobil":
            total_biaya += kelebihan_jam * biaya_mobil_per_jam
        else:
            print("Jenis kendaraan tidak valid! Pilih 'motor' atau 'mobil'.")
            return None

    # Cek apakah parkir lebih dari 24 jam
    if total_jam > 24:
        total_biaya += biaya_tambahan_24_jam

    return total_biaya


def main():
    """
    Fungsi utama program untuk input data pengguna dan menampilkan biaya parkir.
    """
    print("=== Program Perhitungan Biaya Parkir Stasiun ===\n")

    # Input dari pengguna
    try:
        jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil): ").lower()
        total_jam = int(input("Masukkan total durasi parkir (jam): "))

        # Validasi input jam parkir
        if total_jam < 0:
            print("Durasi parkir tidak bisa negatif!")
            return

        # Menghitung biaya parkir
        total_biaya = hitung_biaya_parkir(jenis_kendaraan, total_jam)

        # Menampilkan hasil
        if total_biaya is not None:
            print(f"\nTotal biaya parkir untuk {jenis_kendaraan} selama {total_jam} jam adalah: Rp{total_biaya:,}")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka untuk durasi parkir.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
