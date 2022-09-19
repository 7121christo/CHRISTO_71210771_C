#71210771 - CHRISTOPHORUS ADYATMA WAHYU SETYA NAYOTTAMA

import json

with open('mahasiswa.json', 'r') as datafile:
    data = json.load(datafile)
data={}

jumlahmhs = int(input("Masukkan jumlah mahasiswa baru : "))

for i in range(jumlahmhs):
    nama=str(input("Masukkan nama Anda : "))
    isian=[]
    kamu={}
    jumlahhobi=int(input("Masukkan jumlah hobi : "))
    isihobi=[]
    for i in range(jumlahhobi):
        hobi=str(input("Masukan Hobi : "))
    prestasi=input("Masukkan Prestasi Anda : ")

    isian.append({"BioData":{"Hobi":isihobi,"Prestasi":prestasi}})
    data[nama] = isian

    print("=== Data berhasil ditambahkan ===")


with open('mahasiswa.json', 'w') as datafile:
    json.dump(data, datafile)
