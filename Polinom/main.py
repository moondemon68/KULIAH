# PROGRAM polinom
# Menjumlahkan, mengurangi dan menurunkan polinom

# KAMUS
# p1,p2                         : array of integer
# derajat1,derajat2,koef,der,opt: integer

def cetak(p,n):
    # PROGRAM cetak
    # Mencetak polinom

    # KAMUS LOKAL
    # p: array of integer
    # n: integer

    # ALGORITMA
    for i in range(n,-1,-1):
        #menulis operator jika i<n
        if ((p[i]>0)and(i!=n)):
            print(" + ",end="")
        elif ((p[i]<0)and(i!=n)):
            print(" - ",end="")

        #menulis koefisien
        if (i==n):
            if (abs(p[i])==1) and (n>0):
                if (p[i]==-1):
                    print("-",end="")
                #p[i]==1 tidak print apa-apa
            else:
                print(p[i],end="")
        elif ((abs(p[i])!=1)and(p[i]!=0)) or ((abs(p[i])==1)and(i==0)): #i!=n
            print(abs(p[i]),end="")

        #menulis variabel
        if ((i>0) and (p[i]!=0)):
            if (i==1):
                print("x",end="")
            else:
                print("x^"+str(i),end="")
    print()

def tambahkurang(P1, P2, mult):    # P1, P2 : array koefisien polinom
    # PROGRAM tambahkurang
    # Menjumlahkan/mengurangi polinom 1 dengan polinom 2

    # KAMUS LOKAL
    # P1,P2: array of integer
    # mult : integer

    # ALGORITMA
    P3 = [0 for i in range(100)]
    derajat3=0
    for i in range(100):
        P3[i] = P1[i] + P2[i]*mult
        if (P3[i]!=0):
            derajat3=i
    cetak(P3,derajat3)

def turunan(p,n):    #p: array koef polinom, n: derajat polinom
    # PROGRAM turunan
    # Menghitung turunan dari suatu polinom

    # KAMUS LOKAL
    # p: array of integer
    # n: integer
    # Turunan polinom dengan mengalikan derajat dengan koefisien serta mengurangi 1 derajatnya
    for i in range(1,n+1):
        p[i-1]=p[i]*i
    # Mencetak hasil turunan
    if (n>0):
        cetak(p,n-1)
    else:
        cetak(p,n)

#ALGORITMA
print("PROGRAM START")

p1=[0 for i in range(100)]  #insialisasi polinom 1
derajat1=0  #insialisasi derajat polinom 1
koef=0      #insialisasi variabel koef
der=0       #insialisasi variabel der
print("Mulai pembacaan polinom 1.")
while (der!=-999): #membaca pasangan bilangan selama koefisien tidak bernilai -999
    der,koef=[int(x) for x in input("Masukkan pasangan derajat dan koefisien polinom 1: ").split()]
    #membaca pasangan bilangan, lalu mensplit input ke dalam variabel der dan koef
    if ((der!=-999) and (der>=0)): #derajat tidak boleh bernilai negatif
        p1[der]=koef    #memasukkan data polinom ke dalam array
        if ((p1[der]!=0) and (der>derajat1)):
            derajat1=der    #mengupdate derajat polinom
print("Pembacaan polinom 1 dihentikan.")

p2=[0 for i in range(100)]  #insialisasi polinom 2
derajat2=0  #insialisasi derajat polinom 2
koef=0      #insialisasi variabel koef
der=0       #insialisasi variabel der
print("Mulai pembacaan polinom 2.")
while (der!=-999): #membaca pasangan bilangan selama koefisien tidak bernilai -999
    der,koef=[int(x) for x in input("Masukkan pasangan derajat dan koefisien polinom 2: ").split()]
    #membaca pasangan bilangan, lalu mensplit input ke dalam variabel der dan koef
    if ((der!=-999) and (der>=0)): #derajat tidak boleh bernilai negatif
        p2[der]=koef    #memasukkan data polinom ke dalam array
        if ((p2[der]!=0) and (der>derajat2)):
            derajat2=der    #mengupdate derajat polinom
print("Pembacaan polinom 2 dihentikan.")
print("================================================================")   #pembatas antara pembacaan input dan pemilihan program

opt=1   #insialisasi varibel opt (menu yang akan dipilih)
while (opt!=0):
    print("Pilih menu:")
    print("Menu 1 : mencetak nilai polinom P1 dan P2")
    print("Menu 2 : menjumlahkan polinom P1 dan P2 dan menuliskan hasilnya")
    print("Menu 3 : mengurangi polinom P1 dengan P2 dan menuliskan hasilnya")
    print("Menu 4 : membuat turunan dari P1 dan P2 dan menuliskan hasilnya")
    print("Menu 0 : mengakhiri program")
    opt=int(input("Masukkan menu: "))
    if (opt==1):
        print("P1: ",end="")
        cetak(p1,derajat1)  #memanggil fungsi cetak untuk mencetak polinom 1
        print("P2: ",end="")
        cetak(p2,derajat2)  #memanggil fungsi cetak untuk mencetak polinom 2
    elif (opt==2):
        tambahkurang(p1,p2,1)   #memanggil fungsi tambahkurang, dengan pengali bernilai 1
    elif (opt==3):
        tambahkurang(p1,p2,-1)  #memanggil fungsi tambahkurang, dengan pengali bernilai -1
    elif (opt==4):
        print("Turunan P1: ",end="")
        turunan(p1,derajat1)    #memanggil fungsi turunan untuk mencetak turunan polinom 1
        print("Turunan P2: ",end="")
        turunan(p2,derajat2)    #memanggil fungsi turunan untuk mencetak turunan polinom 2
    elif (opt==0):
        print("Program akan keluar. Terima kasih.") #tidak ada pemanggilan fungsi, program berhenti
    else:
        print("Maaf, menu yang Anda masukkan salah.") #tidak ada pemanggilan fungsi, program masih berjalan
    print("================================================================")   #pembatas antar menu
