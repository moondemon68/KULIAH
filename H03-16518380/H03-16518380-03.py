# Program Soal3
# Menentukan KPK dari tiga buah bilangan
# KAMUS
# a,b,c: integer

def fpb(a,b):
    # Menentukan faktor persekutuan terbesar dari dua buah bilangan
    # KAMUS LOKAL
    # mini,a,b: integer
    # ALGORITMA
    mini=a                  # Mini menyimpan angka yang lebih kecil dari a
    if (b<mini):
        mini=b              # Mini mengubah bilangan menjadi b bila b lebih kecil dari mini (a)
    for i in range(mini,0,-1):
        if (a%i==0 and b%i==0):
            return i        # Mengembalikan bilangan terbesar yang dapat membagi a dan b

def kpk2(a,b):
    # Menentukan faktor persekutuan terbesar dari dua buah bilangan
    # KAMUS LOKAL
    # a,b: integer
    # ALGORITMA
    return a*b//fpb(a,b)    # Kpk dari 2 bilangan adalah hasil kali kedua bilangan tersebut dibagi fpbnya

def kpk3(a,b,c):
    # Menentukan faktor persekutuan terbesar dari dua buah bilangan
    # KAMUS LOKAL
    # a,b,c: integer
    # ALGORITMA
    a=kpk2(a,b)             # Variabel a diubah menjadi kpk dari a dan b
    return kpk2(a,c)        # Mengembalikan kpk dari a (kpk dari a dan b) dan c

a=int(input("Masukkan bilangan A: "))   # Input angka a
b=int(input("Masukkan bilangan B: "))   # Input angka b
c=int(input("Masukkan bilangan C: "))   # Input angka c
print("KPK dari "+str(a)+', '+str(b)+', dan '+str(c)+' adalah '+str(kpk3(a,b,c))+'.')   # Mengoutputkan kpk dari a,b dan c
