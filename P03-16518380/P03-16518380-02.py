# NIM/Nama	: Morgen Sudyanto
# Tanggal	: 3 Oktober 2018
# Deskripsi	: Soal latihan nomor 2

# Program jumlahHex
# Menjumlahkan 2 buah bilangan Hexadecimal (basis 16)

# KAMUS
# a1,a2,b1,b2: char
# a,b,c: int

def convHexToInt(a):
	# Program konversiHexKeInt
	# Mengonversikan sebuah karakter heksadesimal (basis 16) menjadi integer (basis 10)
	
	# KAMUS LOKAL
	# a: char
	
	# ALGORITMA
	if (a=='0'):
		return 0
	if (a=='1'):
		return 1
	if (a=='2'):
		return 2
	if (a=='3'):
		return 3
	if (a=='4'):
		return 4
	if (a=='5'):
		return 5
	if (a=='6'):
		return 6
	if (a=='7'):
		return 7
	if (a=='8'):
		return 8
	if (a=='9'):
		return 9
	if (a=='A'):
		return 10
	if (a=='B'):
		return 11
	if (a=='C'):
		return 12
	if (a=='D'):
		return 13
	if (a=='E'):
		return 14
	if (a=='F'):
		return 15

def convIntToHex(a):
	# Program konversiIntKeHex
	# Mengonversikan sebuah integer (basis 10) menjadi hexadecimal (basis 16)
	
	# KAMUS LOKAL
	# a: int
	
	# ALGORITMA
	if (a==0):
		return '0'
	if (a==1):
		return '1'
	if (a==2):
		return '2'
	if (a==3):
		return '3'
	if (a==4):
		return '4'
	if (a==5):
		return '5'
	if (a==6):
		return '6'
	if (a==7):
		return '7'
	if (a==8):
		return '8'
	if (a==9):
		return '9'
	if (a==10):
		return 'A'
	if (a==11):
		return 'B'
	if (a==12):
		return 'C'
	if (a==13):
		return 'D'
	if (a==14):
		return 'E'
	if (a==15):
		return 'F'

# ALGORITMA
a=0												# inisialisasi bilangan A
a1=input("Masukkan digit pertama bilangan A: ")	# menginput digit pertama bilangan A
a+=convHexToInt(a1) 							# konversikan digit ke 1, lalu tambahkan ke variabel a
a*=16											# digit pertama dikalikan dengan 16, karena bilangan hexadecimal memiliki basis 16
a2=input("Masukkan digit kedua bilangan A: ")	# menginput digit kedua bilangan A
a+=convHexToInt(a2) 							# konversikan digit ke 2, lalu tambahkan ke variabel a

b=0												# inisialisasi bilangan B
b1=input("Masukkan digit pertama bilangan B: ")	# menginput digit pertama bilangan B
b+=convHexToInt(b1) 							# konversikan digit ke 1, lalu tambahkan ke variabel b
b*=16											# digit pertama dikalikan dengan 16, karena bilangan hexadecimal memiliki basis 16
b2=input("Masukkan digit kedua bilangan B: ")	# menginput digit kedua bilangan B
b+=convHexToInt(b2)								# konversikan digit ke 2, lalu tambahkan ke variabel b

c=a+b											# hasil penjumlahan desimal A dan B disimpan pada variabel c
print(a1+a2+" + "+b1+b2+" = "+convIntToHex(c//16)+convIntToHex(c%16))	# Mengeluarkan hasil sesuai dengan format output yang diberikan
