# NIM/Nama	: Morgen Sudyanto
# Tanggal	: 3 Oktober 2018
# Deskripsi	: Soal latihan nomor 1

# Program konversi
# Mengonversikan sebuah karakter heksadesimal (basis 16) menjadi integer (basis 10)

# KAMUS
# c: char

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

# ALGORITMA
c=input("Masukkan karakter heksadesimal: ")				# Menginputkan hexadecimal yang ingin diubah
print("Representasi desimalnya "+str(convHexToInt(c)))  # Mengeluarkan integer hasil konversi
