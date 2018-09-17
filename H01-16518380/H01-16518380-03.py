# NIM/Nama	: Morgen Sudyanto
# Tanggal	: 08/09/2018
# Deskripsi	: Mencari siapa pemenang perolehan medali antara Jawa Tengah, Jawa Barat dan DKI Jakarta

#KAMUS
#t1 : int
#t2 : int
#t3 : int
#b1 : int
#b2 : int
#b3 : int
#j1 : int
#j2 : int
#j3 : int
#t : int
#b : int
#j : int
#st : int
#sb : int
#sj : int

t3=int(input("Masukkan perolehan emas Jawa Tengah: "))
t2=int(input("Masukkan perolehan perak Jawa Tengah: "))
t1=int(input("Masukkan perolehan perunggu Jawa Tengah: "))
b3=int(input("Masukkan perolehan emas Jawa Barat: "))
b2=int(input("Masukkan perolehan perak Jawa Barat: "))
b1=int(input("Masukkan perolehan perunggu Jawa Barat: "))
j3=int(input("Masukkan perolehan emas DKI Jakarta: "))
j2=int(input("Masukkan perolehan perak DKI Jakarta: "))
j1=int(input("Masukkan perolehan perunggu DKI Jakarta: "))
print("Pemenangnya adalah ",end="")

#Menghitung skor
t=t3*3+t2*2+t1
b=b3*3+b2*2+b1
j=j3*3+j2*2+j1

#poin provinsi
st=0
sb=0
sj=0
#Bandingkan semua pasang provinsi, dan berikan 2 poin kepada provinsi yang lebih
#unggul. Bila seri, maka berikan kedua provinsi tersebut 1 poin.
if (t==b):
    if (t3==b3):
        if (t2==b2):
            if (t1==b1):
                st+=1;
                sb+=1;
            elif (t1>b1):
                st+=2;
            else:
                sb+=2;
        elif (t2>b2):
            st+=2;
        else:
            sb+=2;
    elif (t3>b3):
        st+=2;
    else:
        sb+=2;
elif (t>b):
    st+=2;
else:
    sb+=2;

if (t==j):
    if (t3==j3):
        if (t2==j2):
            if (t1==j1):
                st+=1;
                sj+=1;
            elif (t1>j1):
                st+=2;
            else:
                sj+=2;
        elif (t2>j2):
            t+=2;
        else:
            sj+=2;
    elif (t3>j3):
        st+=2;
    else:
        sj+=2;
elif (t>j):
    st+=2;
else:
    sj+=2;

if (b==j):
    if (b3==j3):
        if (b2==j2):
            if (b1==j1):
                sb+=1;
                sj+=1;
            elif (b1>j1):
                sb+=2;
            else:
                sj+=2;
        elif (b2>j2):
            sb+=2;
        else:
            sj+=2;
    elif (b3>j3):
        sb+=2;
    else:
        sj+=2;
elif (b>j):
    sb+=2;
else:
    sj+=2;

#print(str(st),str(sb),str(sj))

#Karena dijamin pasti ada salah satu provinsi yang lebih unggul, maka
#dapat dipastikan bahwa salah satu provinsi pasti mendapat poin 4.
if (st==4):
    print("Jawa Tengah.")
if (sb==4):
    print("Jawa Barat.")
if (sj==4):
    print("DKI Jakarta.")
