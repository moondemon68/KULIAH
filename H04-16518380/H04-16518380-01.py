# NIM/Nama  : 16518380/Morgen Sudyanto
# Tanggal   : 22 Oktober 2018
# Deskripsi : Soal 1

import pandas as pd
df=pd.read_csv("stei-b-1.csv")

#SOAL 1
#Banyaknya data
print(len(df));
#9628

#SOAL 2
#Nilai matematika, fisika, dan kimia dari mahasiswa bernama Tuan Yon.
df2=df.loc[df["nama"]=="Tuan Yon"]
print(df2)
#Nilai Matematika =91
#Nilai Fisika = 83
#Nilai Kimia = 63

#SOAL 3
#Banyaknya mahasiswa dengan nilai matematika di atas 80
df3=df.loc[df["nilai_mat"]>80]
print(len(df3))
#2789

#SOAL 4
#Banyaknya mahasiswa yang mendapat nilai kurang dari 40 di matkul apapun
df4=df.loc[(df["nilai_mat"]<40)|(df["nilai_fis"]<40)|(df["nilai_kim"]<40)]
print(len(df4))
#4351

#SOAL 5
#Banyaknya mahasiswa yang mendapat nilai terendah di fisika
minimum=df["nilai_fis"].min()
df5=df.loc[(df["nilai_fis"]==minimum)]
print(len(df5))
#126

#SOAL 6
#Data 10 besar peserta peraih nilai tertinggi di fisika. Jika ada yang nilainya sama, ambil mahasiswa
#dengan nama lebih kecil
df6=df.sort_values(["nilai_fis","nama"],ascending=[0,1])
print(df6[:10])
#                        nama fakultas  nilai_mat  nilai_fis  nilai_kim
#1905           Abdillah Aziz     FTMD         59         99         23
#3489  Agatha Nabilla Lestari     STEI         33         99         81
#5087    Ahmad Zahi Ulul Azmi     FTMD         41         99         81
#2822          Aidah Fithriah     FTMD         85         99         81
#1431                  Albert     FTMD         80         99         25
#5317        Alexander Sukono     FTMD         54         99         81
#6169            Alfred Andry     STEI         94         99         81
#7403    Alief Rizky Ramadhan    SITHR         90         99         81
#3046   Alwidya Angga Safitri     FTSL         40         99         81
#7060  Alyssa Nadhira Windari     FTMD         46         99         81

#SOAL 7
#Tabel frekuensi masing-masing fakultas
print(df["fakultas"].value_counts())
#FTSL     2475
#STEI     2416
#SITHR    2376
#FTMD     2361

#SOAL 8
#Rata-rata dari nilai matematika semua mahasiswa
print(df["nilai_mat"].mean())
#65.24293726630661

#SOAL 9
#Standar deviasi dari nilai fisika semua mahasiswa
print(df["nilai_fis"].std())
#25.7295023400875

#SOAL 10
#Rata-rata dari nilai kimia STEI
df10=df.loc[df["fakultas"]=="STEI"]
print(df10["nilai_kim"].mean())
#50.226407284768214

#SOAL 11
#Dengan nilai manakah (matematika / kimia) nilai fisika berkorelasi? Berapa koefisien korelasinya?
print(df["nilai_fis"].corr(df["nilai_mat"]))
print(df["nilai_fis"].corr(df["nilai_kim"]))
#Koefisien korelasi antara nilai fisika dengan nilai mat: -0.019784122258082976
#Koefisien korelasi antara nilai fisika dengan nilai kim: 0.8246142287210513
#Jadi, nilai fisika berbanding lurus dengan nilai kimia, tetapi tidak berkolerasi dengan nilai mat.
