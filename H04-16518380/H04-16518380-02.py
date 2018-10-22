# NIM/Nama  : 16518380/Morgen Sudyanto
# Tanggal   : 22 Oktober 2018
# Deskripsi : Soal 2

import pandas as pd
df=pd.read_csv("stei-b-2.csv")

#SOAL 1
#Banyaknya data
print(len(df));
#7948

#SOAL 2
#Data penerbangan yang memiliki harga 1.999.999
df2=df.loc[df["harga"]==1999999]
print(df2)
#      maskapai asal tujuan  tahun  penumpang    harga
#3411  rajawali  SRG    BDO   2017        101  1999999

#SOAL 3
#Banyaknya penerbangan dengan harga di atas 3.500.000
df3=df.loc[df["harga"]>3500000]
print(len(df3))
#1255

#SOAL 4
#Banyaknya penerbangan di tahun 2014 dengan asal atau tujuan bukan kota PDG
df4=df.loc[(df["tahun"]==2014)&(df["asal"]!="PDG")&(df["tujuan"]!="PDG")]
print(len(df4))
#1700

#SOAL 5
#Data penerbangan maskapai macan dengan harga minimum
df5a=df.loc[df["maskapai"]=="macan"]
imin=df5a["harga"].idxmin()
print(df[imin:imin+1])
#     maskapai asal tujuan  tahun  penumpang    harga
#6060    macan  JOG    BTH   2014         60  1000420

#SOAL 6
#Data 10 penerbangan rajawali dengan penumpang terbanyak. Jika ada penerbangan yang sama banyak,
#urutkan berdasar harga dari yang termurah
df6a=df.loc[df["maskapai"]=="rajawali"]
df6b=df6a.sort_values(["penumpang","harga"],ascending=[0,1])
print(df6b[:10])
#      maskapai asal tujuan  tahun  penumpang    harga
#7542  rajawali  JOG    HLP   2015        200  3973270
#5711  rajawali  PKU    UPG   2017        200  3974025
#4414  rajawali  CGK    BTH   2017        200  3975674
#2019  rajawali  PKU    PDG   2015        200  3979693
#5712  rajawali  BTO    UPG   2016        200  3979789
#1079  rajawali  CGK    DPS   2016        200  3980820
#1187  rajawali  BTO    PDG   2015        200  3982368
#6425  rajawali  KNO    SRG   2014        200  3982754
#3317  rajawali  KNO    DPS   2015        200  3986952
#2456  rajawali  BDO    SRG   2016        200  3989431

#SOAL 7
#Tabel frekuensi penerbangan country link masing-masing tahun
df7=df.loc[df["maskapai"]=="country link"]
print(df7["tahun"].value_counts())
#2017    437
#2014    414
#2015    374
#2016    366

#SOAL 8
#Rata-rata harga seluruh penerbangan
print(df["harga"].mean())
#2491494.6465777555

#SOAL 9
#Standar deviasi jumlah penumpang maskapai mataram
df9=df.loc[df["maskapai"]=="mataram"]
print(df9["penumpang"].std())
#41.266006289202664

#SOAL 10
#Rata-rata dari harga maskapai country link
df10=df.loc[df["maskapai"]=="country link"]
print(df10["harga"].mean())
#2503205.1458202386

#SOAL 11
#Koefisien korelasi dari jumlah penumpang dengan harga
print(df["harga"].corr(df["penumpang"]))
#0.9745972176473994
#Jadi, jumlah penumpang berbanding lurus dengan harga
