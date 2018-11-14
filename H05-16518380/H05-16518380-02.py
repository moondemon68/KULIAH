# NIM/Nama  : 16518380/Morgen Sudyanto
# Tanggal   : 3 November 2018
# Deskripsi : Soal PR Praktikum 5 No 2

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("stei-b-2.csv")

#1. Banyaknya data
print(len(df))
#9312

#2. Pie chart banyaknya mahasiswa tiap gender
df["gender"].value_counts().plot(kind="pie",title="Pie Chart Gender")
plt.show()

#3. Berdasarkan plot sebelumnya, gender mana yang lebih mayoritas?
#Laki - Laki

#4. Bar chart dengan fakultas sebagai sumbu x dan jumlah mahasiswa dengan tinggi di atas 160 sebagai sumbu y.
df1=df.loc[df["tinggi"]>160]
df1["fakultas"].value_counts().plot(kind="bar",title="Mahasiswa tinggi tiap fakultas")
plt.show()

#5. Histogram dengan tinggi sebagai sumbu x dan jumlah mahasiswa laki-laki sebagai sumbu y.
df1=df.loc[df["gender"]=="M"]
df1[["tinggi"]].plot(kind="hist", bins =[150,155,160,165,170,175,180,185],rwidth=0.5,title="Histogram Tinggi")
plt.show()

#6. Stacked bar chart dengan fakultas sebagai sumbu x dan jumlah mahasiswa tiap gender sebagai stacked sumbu y.
df.groupby(["fakultas","gender"])["nama"].size().unstack().plot(kind="bar",stacked=True,title="Jumlah mahasiswa tiap gender tiap fakultas")
plt.show()

#7. Berdasar plot sebelumnya, fakultas mana yang rasio mahasiswa perempuannya paling banyak dibanding fakultas lain?
#SITHR

#8. Line chart dengan berat badan sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y.
df1=df['berat'].value_counts().rename_axis('berat').reset_index(name='counts')
df1=df1.sort_values(["berat"],ascending=[0])
df1.plot(kind="line",x="berat",y="counts",title="Berat mahasiswa")
plt.show()

#9. Line chart seperti soal sebelumnya, namun terdapat 2 garis, masing-masing untuk tiap gender.
df.groupby(["berat","gender"])["nama"].size().unstack().plot(kind="line",stacked=False,title="Berat mahasiswa tiap gender")
plt.show()

#10. Berdasar plot sebelumnya, gender manakah yang cenderung memiliki berat lebih ringan?
#Perempuan

#11. Scatter plot dengan berat badan sebagai sumbu x dan tinggi badan sebagai sumbu y
df.plot(kind="scatter",x="berat",y="tinggi")
plt.show()
