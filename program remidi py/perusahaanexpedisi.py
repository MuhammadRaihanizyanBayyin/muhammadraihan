# Program Perhitungan Biaya Pengiriman Paket
# Layanan ini hanya berlaku untuk area Kota dan Kabupaten Pasuruan

def hitung_biaya_pengiriman(panjang, lebar, tinggi, berat):
    """
    Fungsi untuk menghitung biaya pengiriman paket berdasarkan dimensi dan berat.
    
    Parameter:
    panjang (float): Panjang paket dalam cm.
    lebar (float): Lebar paket dalam cm.
    tinggi (float): Tinggi paket dalam cm.
    berat (float): Berat paket dalam kg.

    Return:
    total_biaya (float): Total biaya pengiriman paket.
    """
    # Tarif biaya
    biaya_per_kg_kecil = 5000           # Biaya per kg untuk paket kecil
    biaya_per_kg_besar = 7000           # Biaya per kg untuk paket besar
    biaya_tambahan_besar = 50000        # Biaya tambahan untuk paket besar
    minimal_biaya = 8000                # Biaya minimal pengiriman

    # Menentukan ukuran paket: Kecil atau Besar
    if panjang <= 50 and lebar <= 50 and tinggi <= 50:
        biaya_per_kg = biaya_per_kg_kecil  # Paket kecil
        biaya_tambahan = 0
    else:
        biaya_per_kg = biaya_per_kg_besar  # Paket besar
        biaya_tambahan = biaya_tambahan_besar

    # Menentukan berat minimal: Berat kurang dari 1 kg dianggap 1 kg
    if berat < 1:
        berat = 1

    # Menghitung total biaya pengiriman
    total_biaya = (biaya_per_kg * berat) + biaya_tambahan

    # Memastikan biaya pengiriman tidak kurang dari biaya minimal
    if total_biaya < minimal_biaya:
        total_biaya = minimal_biaya

    return total_biaya


# Bagian utama program
def main():
    """
    Fungsi utama program untuk menerima input pengguna dan menampilkan total biaya pengiriman.
    """
    print("=== Program Perhitungan Biaya Pengiriman Paket ===")
    print("Catatan: Layanan hanya tersedia untuk Kota dan Kabupaten Pasuruan\n")

    # Input dimensi paket dari pengguna
    try:
        print("Masukkan dimensi paket (dalam cm) dan berat (dalam kg):")
        panjang = float(input("Panjang: "))
        lebar = float(input("Lebar: "))
        tinggi = float(input("Tinggi: "))
        berat = float(input("Berat: "))

        # Input lokasi tujuan
        kota = input("Masukkan kota tujuan: ").lower()

        # Validasi lokasi tujuan (hanya Kota/Kabupaten Pasuruan)
        if kota not in ["kota pasuruan", "kabupaten pasuruan"]:
            print("Maaf, layanan hanya tersedia di Kota dan Kabupaten Pasuruan.")
            return  # Mengakhiri program jika lokasi tidak valid

        # Memanggil fungsi hitung_biaya_pengiriman untuk menghitung biaya
        total_biaya = hitung_biaya_pengiriman(panjang, lebar, tinggi, berat)

        # Menampilkan hasil perhitungan
        print(f"\nTotal biaya pengiriman: Rp{total_biaya:,.0f}")
    except ValueError:
        # Penanganan error jika input bukan angka
        print("Input tidak valid! Harap masukkan angka yang benar untuk dimensi dan berat.")

# Memastikan program berjalan hanya jika dijalankan langsung
if __name__ == "__main__":
    main()
