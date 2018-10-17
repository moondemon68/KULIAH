# NIM/NAMA	: 16518380/Morgen Sudyanto
# Tanggal	: 17 Oktober 2018
# Deskripsi	: Soal nomor 1 Praktikum 4

import pandas as pd

df=pd.read_csv("stei-b.csv")	#membuat dataframe berdasarkan file csv yang diberikan

#SOAL 1
#Banyaknya data

print(len(df))	
#mengoutputkan banyaknya data pada dataframe

#10000

#SOAL 2
#Transaksi yang dilakukan oleh Tuan Yon

no2=df.loc[df["nama"]=="Tuan Yon"]	
#membuat dataframe baru (bernama no2) yang berisi data dimana kolom nama berisi "Tuan Yon"
print(len(no2))	
#mengoutputkan banyaknya data pada dataframe no2 tersebut

#1

#SOAL 3
#Banyaknya transaksi dengan profit di atas 150.000
no3=df.loc[df["profit"]>=150000]	
#membuat dataframe baru (bernama no3) yang berisi data dimana kolom profit berisi angka yang lebih besar dari 150000
print(len(no3))	
#mengoutputkan banyaknya data pada dataframe no3 tersebut

#2656

#SOAL 4
#Banyaknya transaksi di bulan Oktober 2014 dengan quantitiy kurang dari 10

no4=df.loc[(df["bulan"]==10)&(df["tahun"]==2014)&(df["qty"]<10)]	
#membuat dataframe baru (bernama no4) yang berisi data dimana kolom bulan berisi angka 10, 
#kolom tahun berisi angka 2014 dan kolom qty berisi angka yang lebih kecil dari 10
print(len(no4))
#mengoutputkan banyaknya data pada dataframe no4 tersebut

#45

#SOAL 5
#Banyaknya transaksi makanan dengan profit minimum

no5=df.loc[(df["tipe_barang"]=="makanan")]
#membuat dataframe baru (bernama no5) yang berisi data dimana kolom tipe_barang berisi "makanan"
minprof=no5.loc[no5["profit"].idxmin(),"profit"]
#membuat sebuah variabel integer yang berisi minimum dari seluruh data profit dari dataframe no5
no5b=no5.loc[no5["profit"]==minprof]
#membuat dataframe baru (bernama no5b) yang berisi data dimana kolom profit dari dataframe no5 adalah minprof
print(len(no5b))
#mengoutputkan banyaknya data pada dataframe no5b tersebut

#1

#SOAL 6
#Data 10 transaksi alat makan dengan profit terbesar di tahun 2017

no6=df.loc[(df["tipe_barang"]=="alat makan") & (df["tahun"]==2017)]
#membuat dataframe baru (bernama no6) yang berisi data dimana kolom "tipe_barang" berisi "alat makan" dan kolom "tahun" berisi 2017 
no6=no6.sort_values(["profit"],ascending=[0])
#mengurutkan dataframe no6 secara terurut menurun berdasarkan value dari kolom "profit"
print(no6[0:10])
#mengoutputkan 10 data pertama dari dataframe no6 tersebut.

#                            nama tipe_barang  bulan  tahun  qty  profit
#1433      Elfa Norisda Aulianisa  alat makan     12   2017   20  197810
#6122       Rian Jamaludin Pogram  alat makan      4   2017   20  196871
#8393       Destria Nur Imaniarti  alat makan      8   2017   20  196614
#2557               Raihan Faisya  alat makan      7   2017   20  196324
#1926  Muhammad Fikry Nashiruddin  alat makan      6   2017   20  193587
#7602            Okaswara Perkasa  alat makan      1   2017   20  192937
#4016           Hary Yady Pratama  alat makan     11   2017   19  188155
#9100             Nadiya Azkanisa  alat makan      2   2017   19  187000
#6021            Amelinda A A V K  alat makan      1   2017   19  186531
#3413        Muhammad Arif Furqon  alat makan     10   2017   19  183769

#SOAL 7
#Tabel frekuensi masing-masing tahun

no7=df["tahun"].value_counts()
#membuat dataframe baru (bernama no7) yang berisi tabel frekuensi masing-masing tahun 
print(no7)
#mengoutputkan dataframe no7 tersebut

#2010    1300
#2015    1290
#2012    1281
#2013    1250
#2017    1238
#2014    1226
#2016    1213
#2011    1202

#SOAL 8
#Rata-rata profit di bulan Desember 2016

no8=df.loc[(df["bulan"]==12) & (df["tahun"]==2016)]
#membuat dataframe baru (bernama no8) yang berisi data dimana kolom "bulan" berisi 12 dan kolom "tahun" berisi 2016 
ratarata=no8["profit"].mean()
#membuat varibel baru bernama ratarata yang isinya adalah rata-rata dari seluruh profit dataframe no8
print(ratarata)
#mengoutputkan hasilnya

#106113.73809523809

#SOAL 9
#Standar deviasi dari profit transaksi pakaian

no9=df.loc[(df["tipe_barang"]=="pakaian")]
#membuat dataframe baru (bernama no9) yang berisi data dimana kolom "tipe_barang" berisi "pakaian"
stdeviasi=no9["profit"].std()
#membuat varibel baru bernama stdeviasi yang isinya adalah standar deviasi dari seluruh profit dataframe no9
print(stdeviasi)
#mengoutputkan hasilnya

#55454.802489044356

#SOAL 10
#Rata-rata dari profit transaksi pakaian sebelum tahun 2016

no10=df.loc[(df["tipe_barang"]=="pakaian") & (df["tahun"]<2016)]
#membuat dataframe baru (bernama no9) yang berisi data dimana kolom "tipe_barang" berisi "pakaian"  dan kolom "tahun" berisi 2016
ratarata=no10["profit"].mean()
#membuat varibel baru bernama ratarata yang isinya adalah rata-rata dari seluruh profit dataframe no10
print(ratarata)
#mengoutputkan hasilnya

#105296.03875134554

#SOAL 11
#Koefisien korelasi dari quantity dengan profit 

cor=df["profit"].corr(df["qty"])
#membuat varibel baru bernama cor yang isinya adalah koefisien korelasi antara quantity dengan profit dari seluruh dataframe
print(cor)
#mengoutputkan hasilnya

#0.9983687460949128
