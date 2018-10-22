def cetak(p,n):     #p: array koef polinom, n: derajat polinom
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
        if ((i!=0)and(p[i]!=0)):
            print("x^"+str(i),end="")
    print()

derajat=int(input("Masukkan derajat polinom: "))
polinom=[0 for i in range(100)]
for i in range(derajat,-1,-1):
    polinom[i]=int(input("Masukkan koefisien x^"+str(i)+": "))

cetak(polinom,derajat)
