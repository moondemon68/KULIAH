# NIM/NAMA: 16518380/Morgen Sudyanto
# Tanggal:19 September 2018
# Deskripsi: Menghitung jumlah jodoh

#PROGRAM Penjodohan

#KAMUS
#n: int 
#l: array of int
#m: int
#p: array of int
#x: int
#ans: int

#ALGORITMA
n=int(input("Masukkan jumlah laki-laki: "))
l=[0 for i in range(n)]
for i in range(n):
	l[i]=int(input("Masukkan tingkat kegantengan "+str(i+1)+": "))

m=int(input("Masukkan jumlah perempuan: "))
p=[0 for i in range(m)]
for i in range(m):
	p[i]=int(input("Masukkan tingkat kecantikan "+str(i+1)+": "))

x=int(input("Masukkan nilai X: "))

ans=0
for i in range(n):
	for j in range(m):
		if (l[i]+p[j]==x):
			ans+=1;		#increment variabel ans bila kegantengan + kecantikan = x

print("Jumlah pasangan yang jodoh ada "+str(ans)+".")

#python3 P02-16518380-01.py
