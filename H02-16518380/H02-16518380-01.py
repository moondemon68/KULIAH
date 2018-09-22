# NIM/Nama  : Morgen Sudyanto
# Tanggal   : 22 September 2018
# Deskripsi : Mencari FPB dari n buah bilangan

#KAMUS
# n,minimum,FPB  :int
# habis          :bool
# fakultas       : array of int

#ALGORITMA
n=int(input("Masukkan jumlah fakultas: "))
minimum=1000000007  #untuk mencari nilai minimum array
fakultas=[0 for i in range(n)]
for i in range (n):
    fakultas[i]=int(input("Jumlah mahasiswa dari fakultas "+str(i+1)+": "))
    if (fakultas[i]<minimum):   #update nilai minimum
        minimum=fakultas[i];

FPB=0   #faktor persekutuan terbesar dari angka-angka pada array
for i in range (1,minimum+1):
    habis=True     #pendanda apakah semua angka pada array habis dibagi i
    for j in range (n):
        if (fakultas[j]%i!=0):
            habis=False     #jika tidak habis dibagi, maka i tidak mungkin menjadi FPBnya
    if (habis):
        FPB=i   #jika habis membagi, maka i bisa menjadi kandidat FPB (tetapi bisa berubah bila ada bilangan i yang lebih besar dan memenuhi)

print("Jumlah anggota tim terbanyak yang mungkin adalah "+str(FPB))
