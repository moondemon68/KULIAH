# NIM/Nama  : Morgen Sudyanto
# Tanggal   : 22 September 2018
# Deskripsi : Mencari FPB dari n buah bilangan

#KAMUS
# n,minimum,FPB  :int
# habis          :bool
# fakultas       : array of int

#ALGORITMA
n=int(input("Masukkan jumlah fakultas: "))
minimum=1000000007
fakultas=[0 for i in range(n)]
for i in range (n):
    fakultas[i]=int(input("Jumlah mahasiswa dari fakultas "+str(i+1)+": "))
    if (fakultas[i]<minimum):
        minimum=fakultas[i];

FPB=0
for i in range (1,minimum+1):
    habis=True
    for j in range (n):
        if (fakultas[j]%i!=0):
            habis=False
    if (habis):
        FPB=i

print("Jumlah anggota tim terbanyak yang mungkin adalah "+str(FPB))
