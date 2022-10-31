class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
       #pass
       #tulis kode anda di sini
        self._head = None
        self._tail = None
        self._data = []
        self._ukuran = Kasir.DEFAULT_CAPACITY
       

       
    def __len__(self): #mengembalikan ukuran Queue
        #pass
        # tulis kode anda di sini
        return len(self._data)

    def is_empty(self): #mengecek apakah Queue kosong ?
        #pass
        # tulis kode anda di sini
        return len(self._data)

    def dequeue(self): #menghapus data paling depan (front)
        #pass
        # tulis kode anda di sini
        data = self._data[0]
        self._data.remove(data)
        print("### Pelanggan ",data," Selesai Membayar ###")
        return data

    def enqueue(self, namaPelanggan): #menambah data ke list
        #pass
        # tulis kode anda di sini
        self._data.append(namaPelanggan)

    def resize(self, cap): #mengubah ukuran queue pada list
        #pass
        # tulis kode anda di sini
        self._ukuran = self._ukuran * cap
        print("### Melakukan Resize ###")

    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        #pass
        # tulis kode anda di sini
        if len(self._data) > self._ukuran:
            self.resize(2)
        print("=== Kasir ===")
        ukuran = len(self._data)-1
        nomor = 1
        for i in range(0, (self._ukuran)):            
            if i <= ukuran:
                print(nomor,".",self._data[i], end=' ')
                print()
            else:
                print(nomor,". Kosong")
            nomor += 1

        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

