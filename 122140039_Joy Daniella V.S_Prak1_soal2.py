import math

def hitung_luas_dan_keliling_lingkaran(jari_jari):
    # Menangani input yang tidak valid (nilai negatif)
    if jari_jari < 0:
        print("Jari-jari lingkaran tidak boleh negatif")
        return
    
    # Menghitung luas lingkaran
    luas = math.pi * jari_jari**2
    
    # Menghitung keliling lingkaran
    keliling = 2 * math.pi * jari_jari
    
    # Menampilkan hasil
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas:.2f}")
    print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah: {keliling:.2f}")

# Menerima input dari pengguna
try:
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    # Memanggil fungsi untuk menghitung dan mencetak luas serta keliling lingkaran
    hitung_luas_dan_keliling_lingkaran(jari_jari)
except ValueError:
    print("Masukkan harus berupa angka")

