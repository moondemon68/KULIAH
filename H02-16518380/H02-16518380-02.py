# NIM/Nama  : Morgen Sudyanto
# Tanggal   : 22 September 2018
# Deskripsi : Menentukan hasil perkalian polinom

#PROGRAM POLINOM
#KAMUS
# derajatF,derajatG  :int
# F,G,FxG            : array of int

#ALGORITMA
derajatF=int(input("Masukkan derajat f: "))
F=[0 for i in range(derajatF+1)]
for i in range(derajatF,-1,-1): #koefisien diinput dari derajat sampai 0
    F[i]=int(input("Masukkan koefisien x^"+str(i)+": "))
 derajatG=int(input("Masukkan derajat g: "))
G=[0 for i in range(derajatG+1)]
for i in range(derajatG,-1,-1): #koefisien diinput dari derajat sampai 0
    G[i]=int(input("Masukkan koefisien x^"+str(i)+": "))
 FxG=[0 for i in range(derajatF+derajatG+1)]
for i in range(derajatF+1):
    for j in range(derajatG+1):
        FxG[i+j]+=F[i]*G[j];    #menambahkan hasil perkalian koefisien ke array jawaban sesuai dengan derajatnya
 print("Hasil perkalian polinom: ")
if (FxG[derajatF+derajatG]<0):  #output menyesuaikan format output
    print("- ",end="")
    FxG[derajatF+derajatG]*=-1
print(str(FxG[derajatF+derajatG])+"x^"+str(derajatF+derajatG)+" ",end="")
for i in range(derajatF+derajatG-1,-1,-1):  #output dikeluarkan dari derajat yang paling tinggi sampai derajat 0
    if (FxG[i]<0):
        print("- ",end="")
        FxG[i]*=-1
    else:
        print("+ ",end="")
    print(str(FxG[i])+"x^"+str(i)+" ",end="")
