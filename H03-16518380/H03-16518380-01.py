def komposit(a):
    cnt=0
    for i in range(1,a+1):
        if (a%i==0):
            cnt+=1;
    if (cnt>2):
        return True
    else:
        return False

def cek(a,b):
    if (komposit(a) and komposit(b) and komposit(a+b)):
        return True
    else:
        return False

a=int(input("Masukkan A: "))
b=int(input("Masukkan B: "))
print("Pasangan bilangan komposit:")
for i in range(a,b+1):
    for j in range(i+1,b+1):
        if (cek(i,j)):
            print(str(i)+" "+str(j))
