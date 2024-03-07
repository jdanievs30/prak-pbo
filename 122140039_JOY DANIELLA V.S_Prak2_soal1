class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def method1(self):
        # Contoh operasi pada method 1
        return f"{self.get_nama()} sedang melakukan operasi 1."

    def method2(self, parameter):
        # Contoh operasi pada method 2
        return f"{self.get_nama()} sedang melakukan operasi 2 dengan parameter: {parameter}."

    def method3(self):
        # Contoh operasi pada method 3
        return f"{self.get_nama()} sedang melakukan operasi 3."

# Inisiasi object pertama dengan semua parameter
mahasiswa1 = Mahasiswa(nim="12345", nama="John Doe", angkatan=2022, isMahasiswa=True)

# Inisiasi object kedua tanpa parameter isMahasiswa
mahasiswa2 = Mahasiswa(nim="67890", nama="Jane Doe", angkatan=2023)

# Penggunaan method pada object pertama
hasil_method1 = mahasiswa1.method1()
hasil_method2 = mahasiswa1.method2("argumen_method2")
hasil_method3 = mahasiswa1.method3()

# Penggunaan method pada object kedua
hasil_method1_mahasiswa2 = mahasiswa2.method1()
hasil_method2_mahasiswa2 = mahasiswa2.method2("argumen_method2_mahasiswa2")
hasil_method3_mahasiswa2 = mahasiswa2.method3()

# Contoh penggunaan getter untuk mendapatkan nilai private property
nama_mahasiswa1 = mahasiswa1.get_nama()
nim_mahasiswa2 = mahasiswa2.get_nim()

print(hasil_method1)
print(hasil_method2)
print(hasil_method3)

print(hasil_method1_mahasiswa2)
print(hasil_method2_mahasiswa2)
print(hasil_method3_mahasiswa2)

print(f"Nama Mahasiswa 1: {nama_mahasiswa1}")
print(f"NIM Mahasiswa 2: {nim_mahasiswa2}")
