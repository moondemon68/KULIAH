# Program Soal2
# Menentukan apakah sepasang bilangan adalah pasangan bilangan PrimaPrima
# KAMUS
# a,b: integer

def prima(a):
    # Menentukan apakah sebuah bilangan adalah bilangan prima
    # KAMUS LOKAL
    # cnt,a: integer
    # ALGORITMA
    cnt=0               #variabel untuk menghitung jumlah faktor dari a
    for i in range(1,a+1):
        if (a%i==0):
            cnt+=1;     #variabel cnt ditambah bila a habis membagi i
    if (cnt==2):
        return True     #bilangan yang memiliki faktor sama dengan 2 adalah bilangan prima
    else:
        return False    #bilangan yang memiliki faktor kurang dari atau lebih dari 2 bukan bilangan prima

def cek(a,b):
    # Menentukan apakah sepasang bilangan adalah sepasang bilangan PrimaPrima
    # KAMUS LOKAL
    # a,b: integer
    # ALGORITMA
    if (prima(a) and prima(b) and prima(10*a+b)):
        return True     #bilangan PrimaPrima adalah bilangan yang a,b dan gabungannya(ab) nya prima
    else:
        return False    #bilangan bukan PrimaPrima adalah bilangan yang a,b atau gabungannya(ab) nya bukan prima

# ALGORITMA
a=int(input("Masukkan A: "))    #input angka A
b=int(input("Masukkan B: "))    #input angka B
print("Pasangan bilangan PrimaPrima:")
for i in range(a,b+1):
    for j in range(a,b+1):                 #bilangan kedua harus lebih besar dari bilangan pertama
        if (cek(i,j)):
            print(str(i)+" "+str(j))       #mengoutputkan pasangan bilangan PrimaPrima
