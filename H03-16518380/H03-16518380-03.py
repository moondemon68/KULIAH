def fpb(a,b):
    mini=a
    if (b<mini):
        mini=b
    for i in range(mini,0,-1):
        if (a%i==0 and b%i==0):
            return i

def kpk2(a,b):
    return a*b//fpb(a,b)

def kpk3(a,b,c):
    a=kpk2(a,b)
    return kpk2(a,c)

a=int(input("Masukkan bilangan A: "))
b=int(input("Masukkan bilangan B: "))
c=int(input("Masukkan bilangan C: "))
print("KPK dari "+str(a)+', '+str(b)+', dan '+str(c)+' adalah '+str(kpk3(a,b,c))+'.')
