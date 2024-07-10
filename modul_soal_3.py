from Soal_3 import Antrian

# Buat antrian baru
antrian = Antrian()

# Tambahkan beberapa pesanan ke antrian
antrian.enqueue("Mie ayam")
antrian.enqueue("Bakso")
antrian.enqueue("Seblak")

print("Antrian:", antrian)  # Output: Antrian: ['Pesanan 1', 'Pesanan 2', 'Pesanan 3']

# Hapus pesanan dari antrian
print("Dihapus:", antrian.dequeue())  # Output: Dihapus: Pesanan 1

print("Antrian:", antrian)  # Output: Antrian: ['Pesanan 2', 'Pesanan 3']

# Cek apakah antrian kosong
print("Apakah kosong?", antrian.is_empty())  # Output: Apakah kosong? False

# Dapatkan jumlah pesanan dalam antrian
print("Jumlah:", antrian.size())  # Output: Jumlah: 2