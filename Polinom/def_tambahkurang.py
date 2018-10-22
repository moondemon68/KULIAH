def cetak(p, n):     #p: array koef polinom, n: derajat polinom
    for i in range(n,-1,-1):
        # Menulis operator jika i < n
        if ((p[i] > 0) and (i != n)):
            print(" + ", end="")
        elif ((p[i] < 0) and (i != n)):
            print(" - ", end="")

        # Menulis koefisien
        if (i == n):
            if (abs(p[i]) == 1) and (n > 0):
                if (p[i] == -1):
                    print("-", end="")
                # p[i] == 1 tidak print apa-apa
            else:
                print(p[i], end="")
        elif ((abs(p[i]) != 1) and (p[i] != 0)) or ((abs(p[i]) == 1) and (i == 0)): # i != n
            print(abs(p[i]),end="")

        # Menulis variabel
        if ((i != 0) and (p[i] != 0)):
            print("x^" + str(i), end="")
    print()

# Input Polinom 1
n1 = int(input("Masukkan derajat polinom: "))
P1 =[0 for i in range(100)]
for i in range(n1,-1,-1):
    P1[i]=int(input("Masukkan koefisien x^"+str(i)+": "))
cetak(P1, n1)

# Input Polinom 2
n2 = int(input("Masukkan derajat polinom: "))
P2 =[0 for i in range(100)]
for i in range(n2,-1,-1):
    P2[i]=int(input("Masukkan koefisien x^"+str(i)+": "))
cetak(P2, n2)

def penjumlahan(P1, P2):    # P1, P2 : array koefisien polinom
    # Menjumlahkan polinom 1 dengan polinom 2
    P3 = [0 for i in range(100)]
    for i in range(100):
        P3[i] = P1[i] + P2[i]
    # Mencetak hasil penjumlahan
    if (n1 > n2):    
        cetak(P3, n1)
    else: # n1 < n2 atau n1 = n2
        cetak(P3, n2)

def pengurangan(P1, P2):   # P1, P2 : array koefisien polinom
    # Mengurangi polinom 1 dengan polinom 2
    P3 = [0 for i in range(100)]
    for i in range(100):
        if (n1 > n2): 
            P3[i] = P1[i] - P2[i]
        else: # n1 < n2 atau n1 = n2
            P3[i] = P2[i] - P1[i]
    # Mencetak hasil pengurangan
    if (n1 > n2):    
        cetak(P3, n1)
    else: # n1 < n2 atau n1 = n2
        cetak(P3, n2)

print("Hasil penjumlahan:")
penjumlahan(P1, P2)

print("Hasil pengurangan:")
pengurangan(P1, P2)