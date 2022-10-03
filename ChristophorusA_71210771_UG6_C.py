#71210771 - Christophorus Adyatma Wahyu Setya Nayottama

class NodeTabungan:
    no_rekening =  None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    
    def insert_head(self,no_rekening,nama,saldo=0):
        baru = NodeTabungan (no_rekening,nama, saldo)
        if self.isEmpty():
            self.head = baru
            self.tail = baru
            self.tail.next = None
        else:
            baru.next = self.head
            self.head = baru
        self.size += 1
        print()
    
    def deleteHead(self, no_rekening,nama,saldo):
        if self.isEmpty() == False:
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                hapus = self.head
                self.head = self.head.next
                del hapus
            self.size -= 1


#    def filter(self):
#        while self.saldo <= 100:
#            if self.size == 1:
#                self.head = None
#                self.tail = None
#            else:
#                bantu = self.head
#                while bantu.next != self.tail:
#                    bantu = bantu.next
#                hapus = self.tail
#                self.tail = bantu
#                self.tail.next = None
#                del hapus
#            self._size -= 1


    def print(self):
        bantu = self.head
        while bantu != None:
            print('\nNorek:',bantu.no_rekening, end=' ')
            print('\nNama: ',bantu.nama, end=' ')
            print('\nSaldo: ',bantu.saldo, end=' ')
            bantu = bantu.next
        print()

slnc=SLNC()
slnc.insert_head(201,'Hanif',250000)
slnc.insert_head(110,'Yudha',150000)
slnc.print()
#slnc.filter(100)
slnc.print()
#slnc.update(200)
#slnc.update(50)
slnc.print()