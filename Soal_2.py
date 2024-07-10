import pandas as pd

# Data tabel
data = [
    ["Mahasiswa 1", 90, 80],
    ["Mahasiswa 2", 50, 60],
    ["Mahasiswa 3", 65, 70]
]

# Buatkan array 2 dimensi
array_2d = pd.DataFrame(data, columns=["Nama", "Algoritma Struktur Data 2", "Matematika Numerik"])

# Tampilkan rata-rata nilai untuk setiap mata kuliah
rata_rata_matkul = array_2d.iloc[:, 1:].mean()
print("Rata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_matkul)

# Tampilkan rata-rata nilai untuk setiap mahasiswa
rata_rata_mahasiswa = array_2d.iloc[:, 1:].mean(axis=1)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(rata_rata_mahasiswa)