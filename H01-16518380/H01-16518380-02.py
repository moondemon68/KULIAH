# NIM/Nama	: Morgen Sudyanto
# Tanggal	: 08/09/2018
# Deskripsi	: Menghitung sisa waktu tidur Tuan Yon

#KAMUS
#h1 : int
#h2 : int
#h3 : int
#m1 : int
#m2 : int
#m3 : int
#s1 : int
#s2 : int
#s3 : int

print("Masukkan waktu sekarang!")
h1=int(input("Jam   : "))
m1=int(input("Menit : "))
s1=int(input("Detik : "))
print("Masukkan waktu alarm!")
h2=int(input("Jam   : "))
m2=int(input("Menit : "))
s2=int(input("Detik : "))

s3=s2-s1
if (s3<0):	#Kalau nilai detik kurang dari 0, kurangi 1 dari menit dan tambahkan 60 ke detik
	s3+=60
	m2-=1
m3=m2-m1
if (m3<0):	#Kalau nilai menit kurang dari 0, kurangi 1 dari jam dan tambahkan 60 ke menit
	m3+=60
	h2-=1
h3=h2-h1
if (h3<0):	#Kalau nilai jam kurang dari 0, tambahkan 24 ke jam (hari baru)
	h3+=24

print("Alarm akan berbunyi dalam",h3,"jam",m3,"menit",s3,'detik lagi.')
