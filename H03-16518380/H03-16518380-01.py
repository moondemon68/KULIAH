# Program Soal1
# Menentukan apakah sepasang bilangan adalah pasangan bilangan KompositKomposit
# KAMUS
# a,b: integer

def komposit(a):
    # Menentukan apakah sebuah bilangan adalah bilangan komposit
    # KAMUS LOKAL
    # cnt,a: integer
    # ALGORITMA
    cnt=0               # Variabel untuk menghitung jumlah faktor dari a
    for i in range(1,a+1):  
        if (a%i==0):
            cnt+=1;     # Variabel cnt ditambah bila a habis membagi i
    if (cnt>2):
        return True     # Bilangan yang memiliki faktor lebih dari 2 adalah bilangan komposit
    else:
        return False    # Bilangan yang memiliki faktor kurang dari atau sama dengan 2 bukan bilangan komposit

def cek(a,b):
    # Menentukan apakah sepasang bilangan adalah sepasang bilangan KompositKomposit
    # KAMUS LOKAL
    # a,b: integer
    # ALGORITMA
    if (komposit(a) and komposit(b) and komposit(a+b)):
        return True     # Bilangan KompositKomposit adalah bilangan yang a,b dan a+b nya komposit
    else:
        return False    # Bilangan bukan KompositKomposit adalah bilangan yang a,b atau a+b nya bukan komposit

# ALGORITMA
a=int(input("Masukkan A: ")) # Input angka A
b=int(input("Masukkan B: ")) # Input angka B
print("Pasangan bilangan komposit:")
for i in range(a,b+1):
    for j in range(i+1,b+1):            # Bilangan kedua harus lebih besar dari bilangan pertama
        if (cek(i,j)):
            print(str(i)+" "+str(j))    # Mengoutputkan pasangan bilangan KompositKomposit
