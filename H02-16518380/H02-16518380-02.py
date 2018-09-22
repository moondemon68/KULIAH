# NIM/Nama  : Morgen Sudyanto
# Tanggal   : 22 September 2018
# Deskripsi : Menentukan hasil perkalian polinom

#KAMUS
# derajatF,derajatG  :int
# F,G,FxG            : array of int

#ALGORITMA
derajatF=int(input("Masukkan derajat f: "))
F=[0 for i in range(derajatF+1)]
for i in range(derajatF,-1,-1):
    F[i]=int(input("Masukkan koefisien x^"+str(i)+": "))

derajatG=int(input("Masukkan derajat g: "))
G=[0 for i in range(derajatG+1)]
for i in range(derajatG,-1,-1):
    G[i]=int(input("Masukkan koefisien x^"+str(i)+": "))

FxG=[0 for i in range(derajatF+derajatG+1)]
for i in range(derajatF+1):
    for j in range(derajatG+1):
        FxG[i+j]+=F[i]*G[j];

print("Hasil perkalian polinom: ")
if (FxG[derajatF+derajatG]<0):
    print("- ",end="")
    FxG[derajatF+derajatG]*=-1
print(str(FxG[derajatF+derajatG])+"x^"+str(derajatF+derajatG)+" ",end="")
for i in range(derajatF+derajatG-1,-1,-1):
    if (FxG[i]<0):
        print("- ",end="")
        FxG[i]*=-1
    else:
        print("+ ",end="")
    print(str(FxG[i])+"x^"+str(i)+" ",end="")
