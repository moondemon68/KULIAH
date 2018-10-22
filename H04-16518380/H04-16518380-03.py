# NIM/Nama  : 16518380/Morgen Sudyanto
# Tanggal   : 22 Oktober 2018
# Deskripsi : Soal 3

import pandas as pd
df=pd.read_csv("stei-b-3.csv")

#SOAL 1
#Banyaknya data
print(len(df));
#9079

#SOAL 2
#Data karyawan bernama Tuan Yon
df2=df.loc[df["nama"]=="Tuan Yon"]
print(df2)
#          nama departemen  tahun_masuk  usia  golongan     gaji
#2227  Tuan Yon  teknologi         2017    31        10  9939125

#SOAL 3
#Banyaknya karyawan dengan usia kurang dari atau sama dengan 30
df3=df.loc[df["usia"]<=30]
print(len(df3))
#1542

#SOAL 4
#Banyaknya karyawan personalia dengan gaji di luar rentang 4 - 5 juta
df4a=df.loc[df["departemen"]=="personalia"]
df4b=df4a.loc[(df4a["gaji"]<4000000)|(df4a["gaji"]>5000000)]
print(len(df4b))
#1122

#SOAL 5
#Data karyawan produksi dengan gaji maksimum
df5a=df.loc[df["departemen"]=="produksi"]
imax=df5a["gaji"].idxmax()
print(df[imax:imax+1])
#                 nama departemen  tahun_masuk  usia  golongan     gaji
#5047  Ario Nuswantoro   produksi         2014    36         3  9995982

#SOAL 6
#Data 10 karyawan teknologi dengan gaji terbanyak. Jika ada gaji yang sama banyak, urutkan dari usia
#yang termuda
df6a=df.loc[df["departemen"]=="teknologi"]
df6b=df6a.sort_values(["gaji","usia"],ascending=[0,1])
print(df6b[:10])
#                         nama departemen  tahun_masuk  usia  golongan     gaji
#3282   Jawahir Asy Mahdy Maro  teknologi         2015    26         1  9996959
#8971         Vania Avviantari  teknologi         2015    35         1  9994946
#4972               Brian Luas  teknologi         2014    26         1  9989154
#6127       Tiara Fahiramadyan  teknologi         2014    46         1  9987370
#6260               Vivi Novia  teknologi         2014    26         1  9986306
#3739            Nana Restiana  teknologi         2016    37         1  9982168
#8275  Rizkiyani Nadifa Puteri  teknologi         2015    26         1  9956570
#3365         Zaki Abdurrasyid  teknologi         2013    50         1  9951235
#7410     Made Santihayu Sukma  teknologi         2015    35         1  9944009
#8194          Naufal Arifandy  teknologi         2013    42         1  9941846

#SOAL 7
#Tabel frekuensi banyaknya karyawan tiap golongan
print(df["golongan"].value_counts())
#9     945
#6     927
#5     925
#2     913
#8     908
#7     905
#1     903
#3     902
#4     876
#10    875

#SOAL 8
#Tabel frekuensi banyaknya karyawan tiap departemen yang masuk sebelum tahun 2015
df8=df.loc[df["tahun_masuk"]<2015]
print(df8["departemen"].value_counts())
#keuangan       546
#marketing      544
#produksi       530
#teknologi      522
#kreatif        501
#personalia     480
#operasional    476

#SOAL 9
#Rata-rata gaji seluruh karyawan
print(df["gaji"].mean())
#5476321.027756361

#SOAL 10
#Standar deviasi usia karyawan operasional
df10=df.loc[df["departemen"]=="operasional"]
print(df10["usia"].std())
#10.436347593016766

#SOAL 11
#Dengan apakah gaji berkorelasi? Usia, tahun masuk, atau golongan? Tuliskan koefisien korelasinya
print(df["gaji"].corr(df["usia"]))
print(df["gaji"].corr(df["tahun_masuk"]))
print(df["gaji"].corr(df["golongan"]))
#Koefisien korelasi antara gaji dengan usia: -0.0144551765207072
#Koefisien korelasi antara gaji dengan tahun masuk: -0.003936498806261882
#Koefisien korelasi antara gaji dengan golongan: -0.8708577012378018
#Jadi, nilai fisika berbanding terbalik dengan golongan, tetapi tidak berkolerasi dengan usia dan tahun masuk.
