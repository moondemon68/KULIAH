# NIM/Nama  : 16518380/Morgen Sudyanto
# Tanggal   : 3 November 2018
# Deskripsi : Soal PR Praktikum 5 No 1

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("stei-b-1.csv")

#1. Banyaknya data
print(len(df))
#9312

#2. Pie chart banyaknya mahasiswa tiap kendaraan yang digunakan untuk berangkat ke kampus.
df["kendaraan"].value_counts().plot(kind="pie",title="Pie Chart Kendaraan")
plt.show()

#3. Pie chart banyaknya mahasiswa tiap tingkat yang berjalan kaki.
df1=df.loc[df["kendaraan"]=="jalan kaki"]
df1["tingkat"].value_counts().plot(kind="pie",title="Pejalan Kaki")
plt.show()

#4. Histogram dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df[["tingkat"]].plot(kind="hist", bins =[2014.5,2015.6,2016.5,2017.5,2018.5],rwidth=0.5,title="Histogram Tingkat")
plt.show ()

#5. Berdasar plot sebelumnya, angkatan berapa yang jumlah mahasiswanya paling banyak?
#2016

#6. Stacked bar chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa tiap kendaraan sebagai stacked sumbu y
df.groupby(["tingkat","kendaraan"])["nama"].size().unstack().plot(kind="bar",stacked=True,title="Jumlah mahasiswa tiap kendaraan")
plt.show()

#7. Berdasar plot sebelumnya, sebutkan trend kendaraan transportasi tiap tingkat!
#2015: Motor > Mobil > Jalan kaki > Angkot
#2016: Motor > Jalan kaki > Angkot > Mobil
#2017: Angkot > Jalan kaki > Motor > Mobil
#2018: Jalan kaki > Angkot > Motor > Mobil

#8. Line chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df1=df['tingkat'].value_counts().rename_axis('tingkat').reset_index(name='counts')
df1=df1.sort_values(["tingkat"],ascending=[0])
df1.plot(kind="line",x="tingkat",y="counts",title="Jumlah mahasiswa tiap tingkat")
plt.show()

#9. Line chart seperti soal sebelumnya, namun terdapat 4 garis, masing-masing untuk tiap kendaraan
df.groupby(["tingkat","kendaraan"])["nama"].size().unstack().plot(kind="line",stacked=False,title="Jumlah mahasiswa tiap kendaraan tiap tingkat")
plt.show()

#10. Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus bertambah?
#Angkot

#11. Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus menurun?
#Motor
