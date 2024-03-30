class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi 
    
    @staticmethod
    def hitung_luas(sisi):
        print(f"Luas Persegi : {sisi * sisi}")

class Lingkaran:
    def __init__(self, jari2):
        self.jari2 = jari2
    
    @staticmethod
    def hitung_luas(jari2):
        print(f"Luas Persegi : {3.14 * jari2 * jari2}")

persegi = Persegi(5)
lingkaran = Lingkaran(3)

Persegi.hitung_luas(persegi.sisi)
Lingkaran.hitung_luas(lingkaran.jari2)
