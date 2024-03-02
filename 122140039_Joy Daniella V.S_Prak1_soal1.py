def hitung_bilangan_ganjil(lower, upper):
    # Mengecek apakah batas bawah dan atas di atas nol
    if lower < 0 or upper < 0:
        print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
        return
    
    # Inisialisasi jumlah bilangan ganjil
    jumlah_ganjil = 0
    
    # Menghitung jumlah bilangan ganjil dalam rentang
    for bilangan in range(lower, upper + 1):
        if bilangan % 2 != 0:
            jumlah_ganjil += 1
    
    # Menampilkan hasil
    print(f"Jumlah bilangan ganjil antara {lower} dan {upper} adalah: {jumlah_ganjil}")

# Menerima input dari pengguna
batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

# Memanggil fungsi untuk menghitung dan mencetak jumlah bilangan ganjil
hitung_bilangan_ganjil(batas_bawah, batas_atas)

