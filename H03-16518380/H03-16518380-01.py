# Program Soal1
# Menentukan apakah sepasang bilangan adalah pasangan bilangan KompositKomposit
# KAMUS
# a,b: integer

def komposit(a):
    # Menentukan apakah sebuah bilangan adalah bilangan komposit
    # KAMUS LOKAL
    # cnt,a: integer
    # ALGORITMA
    cnt=0
    for i in range(1,a+1):
        if (a%i==0):
            cnt+=1;
    if (cnt>2):
        return True
    else:
        return False

def cek(a,b):
    # Menentukan apakah sepasang bilangan adalah sepasang bilangan KompositKomposit
    # KAMUS LOKAL
    # a,b: integer
    # ALGORITMA
    if (komposit(a) and komposit(b) and komposit(a+b)):
        return True
    else:
        return False

# ALGORITMA
a=int(input("Masukkan A: ")) #input angka A
b=int(input("Masukkan B: ")) #input angka B
print("Pasangan bilangan komposit:")
for i in range(a,b+1):
    for j in range(i+1,b+1):
        if (cek(i,j)):
            print(str(i)+" "+str(j)) #mengoutputkan pasangan bilangan KompositKomposit
