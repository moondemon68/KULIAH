# NIM/Nama  : Morgen Sudyanto
# Tanggal   : 22 September 2018
# Deskripsi : Menentukan banyaknya segitiga yang bisa dibentuk

#KAMUS
# stikYon,stikRin,stikMi,jawaban  :int
# Yon,Rin,Mi                      : array of int

#ALGORITMA
stikYon=int(input("Masukkan banyaknya stik Tuan Yon: "))
Yon=[0 for i in range(stikYon)]
print("Masukkan panjang stik Tuan Yon: ")
for i in range(stikYon):
    Yon[i]=int(input())

stikRin=int(input("Masukkan banyaknya stik Nyai Rin: "))
Rin=[0 for i in range(stikRin)]
print("Masukkan panjang stik Nyai Rin: ")
for i in range(stikRin):
    Rin[i]=int(input())

stikMi=int(input("Masukkan banyaknya stik Tuan Mi: "))
Mi=[0 for i in range(stikMi)]
print("Masukkan panjang stik Tuan Mi: ")
for i in range(stikMi):
    Mi[i]=int(input())

print("Daftar segitiga yang dapat dibuat: ")
for i in range(stikYon):
    for j in range(stikRin):
        for k in range(stikMi):
            if (Yon[i]+Rin[j]>Mi[k] and Yon[i]+Mi[k]>Rin[j] and Rin[j]+Mi[k]>Yon[i]):
                print(Yon[i],end=" ")
                print(Rin[j],end=" ")
                print(Mi[k])
