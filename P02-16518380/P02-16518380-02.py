# NIM/NAMA: 16518380/Morgen Sudyanto
# Tanggal:19 September 2018
# Deskripsi: Menulis semua bilangan prima dari A sampai B

#PROGRAM Menulis Prima

#KAMUS
#A: int
#B: int
#prima: bool


#ALGORITMA
A=int(input("Masukkan A: "))
B=int(input("Masukkan B: "))
print("Bilangan prima dari A hingga B:")
for i in range(A,B+1):
	prima=True	#bilangan i dianggap prima
	for j in range(2,i):
		if(i%j==0):
			prima=False		#jika i habis membagi suatu angka diantara 2 sampai i-1, maka bilangan i tidak prima
	if (i==1):
		prima=False		#1 bukan bilangan prima
	if (prima==True):
		print(i)	#keluarkan angka bila prima

	
#python3 P02-16518380-02.py
