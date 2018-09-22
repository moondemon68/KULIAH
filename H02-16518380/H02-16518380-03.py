# NIM/Nama  : Morgen Sudyanto
# Tanggal   : 22 September 2018
# Deskripsi : Menentukan banyaknya segitiga yang bisa dibentuk

#PROGRAM SEGITIGA

#KAMUS
# stikYon,stikRin,stikMi    :int
# Yon,Rin,Mi                : array of int

#ALGORITMA
stikYon=int(input("Masukkan banyaknya stik Tuan Yon: "))
Yon=[0 for i in range(stikYon)]
print("Masukkan panjang stik Tuan Yon: ")
for i in range(stikYon):    #input banyaknya stik Tuan Yon
    Yon[i]=int(input())

stikRin=int(input("Masukkan banyaknya stik Nyai Rin: "))
Rin=[0 for i in range(stikRin)]
print("Masukkan panjang stik Nyai Rin: ")
for i in range(stikRin):    #input banyaknya stik Nyai Rin
    Rin[i]=int(input())

stikMi=int(input("Masukkan banyaknya stik Tuan Mi: "))
Mi=[0 for i in range(stikMi)]
print("Masukkan panjang stik Tuan Mi: ")
for i in range(stikMi):     #input banyaknya stik Tuan Mi
    Mi[i]=int(input())

print("Daftar segitiga yang dapat dibuat: ")
for i in range(stikYon):    #mencoba semua kemungkinan kombinasi stik Yon, Rin dan Mi
    for j in range(stikRin):
        for k in range(stikMi):
            if (Yon[i]+Rin[j]>Mi[k] and Yon[i]+Mi[k]>Rin[j] and Rin[j]+Mi[k]>Yon[i]): #mengikuti syarat segitiga (a+b>c, a+c>b dan b+c>a)
                print(Yon[i],end=" ")   #output dikeluarkan sesuai dengan format output
                print(Rin[j],end=" ")
                print(Mi[k])
