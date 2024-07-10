class Antrian:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        """Tambahkan pesanan baru ke akhir antrian"""
        self.items.append(item)

    def dequeue(self):
        """Hapus antrian dari depan"""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        """Cek apakah antrian kosong"""
        return len(self.items) == 0

    def size(self):
        """Return jumlah pesanan dalam antrian"""
        return len(self.items)

    def __str__(self):
        """Return representasi string dari antrian"""
        return str(self.items)