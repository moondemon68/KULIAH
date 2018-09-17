# NIM/Nama	: Morgen Sudyanto
# Tanggal	: 08/09/2018
# Deskripsi	: Menghitung harga makanan dan minuman

#KAMUS
#n : int
#m : int

print("Menu makanan:\n1. Indomie Single\n2. Indomie Double\n3. Indomie Telor")
n=int(input("Masukkan nomor menu makanan: "))
print("Menu minuman:\n1. Air Putih\n2. Teh Manis\n3. Kopi")
m=int(input("Masukkan nomor menu minuman: "))
print("Biaya yang harus dibayarkan: ",end="")
if ((n==1) and (m==1)):
	print("4000")
if ((n==1) and (m==2)):
	print("6000")
if ((n==1) and (m==3)):
	print("8000")
if ((n==2) and (m==1)):
	print("8000")
if ((n==2) and (m==2)):
	print("10000")
if ((n==2) and (m==3)):
	print("12000")
if ((n==3) and (m==1)):
	print("7000")
if ((n==3) and (m==2)):
	print("9000")
if ((n==3) and (m==3)):
	print("11000")
