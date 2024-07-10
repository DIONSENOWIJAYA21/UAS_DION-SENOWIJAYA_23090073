class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    
    def deskripsi(self):
        return f"{self.nama} {self.warna} dengan {self.rasa} "

# Definisikan kelas anak yang mewarisi dari Kendaraan
class Buah(Mangga):
    def __init__(self, nama, warna, rasa):

    def deskripsi(self):
        return f"{self.merk} {self.tahun} dengan {self.jarak_tempuh} kilometer dan {self.jumlah_pintu} pintu"

# Buat instance dari kelas Mobil
mobilku = Mobil("Toyota", 2020, 4)

# Panggil atribut dan metode dari kelas Mobil
print(mobilku.merk)  # Output: Toyota
print(mobilku.tahun)  # Output: 2020
print(mobilku.jumlah_pintu)  # Output: 4

mobilku.berkendara(100)
print(mobilku.jarak_tempuh)  # Output: 100

print(mobilku.deskripsi())  # Output: Toyota 2020 dengan 100 kilometer dan 4 pintu