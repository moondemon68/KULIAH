# NIM/Nama	: Morgen Sudyanto
# Tanggal	: 08/09/2018
# Deskripsi	: Mengeluarkan nama warna berdasarkan nilai Hue yang diberikan.
# Komentar  : Contoh test case pada problem nomor 4 salah. Seharusnya hue 150 merepresentasikan warna Green. (bukan Cyan).

#KAMUS
#n : int

n=int(input("Masukkan nilai hue: "))
print("Hue",n,"merepresentasikan warna ",end="")
#Mengeluarkan warna sesuai dengan tabel Range Hue-Warna
if (n>=0 and n<=30):
    print("Red.")
elif(n>=31 and n<=90):
    print("Yellow.")
elif(n>=91 and n<=150):
    print("Green.")
elif(n>=151 and n<=210):
    print("Cyan.")
elif(n>=211 and n<=270):
    print("Blue.")
elif(n>=271 and n<=330):
    print("Magenta.")
elif(n>=331 and n<=360):
    print("Red.")
