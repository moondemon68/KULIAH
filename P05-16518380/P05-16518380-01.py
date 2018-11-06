#Disclaimer: GAJELAS SOALNYA, GAADA MODULNYA, SESI MATERI KEPAKE BUAT SERVIS PC KWKWKWKWKWKWKWKKWWKKWKWKKWKWKWKWKKKWKWKWK
#WKWWKKWKWKWOKWOWKAOWOAWKOAWKOAWKAWOKAWOKAWOAWKOAWKAWOKAWOKAWOKAWOAKWOKAWOAWKOAKAWOKAWOKAWOAKOAWKAOWKWOKOAWKOAWOKAWOKAOKA

#NAMA/NIM: Morgen Sudyanto/16518380
#Tanggal: 31 Oktober 2018
#Deskripsi: Plotting data mahasiswa

import matplotlib
import pandas as pd
matplotlib.use('agg')
import matplotlib.pyplot as plt

df=pd.read_csv("stei-b.csv")

#Banyaknya data
print(len(df))
#9061

#Pie chart banyaknya mahasiswa tiap fakultas.
df1=df["fakultas"].value_counts()
df1.plot(kind="pie",title="Pie Chart mahasiswa tiap fakultas")
plt.savefig("2.png",bbox_inches="tight")

#Pie chart banyaknya mahasiswa FTSL berdasarkan tingkat
df1=df.loc[df["fakultas"]=="FTSL"]
df2=df1['tingkat'].value_counts().rename_axis('tingkat').reset_index(name='counts')
df2.plot(kind="pie",x='tingkat',y='counts',title="Pie Chart Tingkat Mahasiswa FTSL(0: 2015,1: 2016,2: 2017,3: 2018")
plt.savefig("3.png",bbox_inches="tight")
#BERMASALAH dalam label

#Histogram dengan IP sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y, gunakan pertambahan 0.5
df[["ip"]].plot(kind="hist",bins=[0,0.5,1,1.5,2,2.5,3,3.5,4],rwidth=0.8,title="HISTOGRAM IP")
plt.savefig("4.png",bbox_inches="tight")

#Berdasar plot sebelumnya, range ip mana yang paling banyak diperoleh?
#3.0 - 3.5

#Stacked bar chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa tiap fakultas sebagai stacked sumbu y
df1=df.groupby(["tingkat","fakultas"])["nama"].size().unstack()
df1.plot(kind="bar",stacked=True)
plt.savefig("6.png",bbox_inches="tight")

# Berdasar plot sebelumnya, angkatan ke berapa STEI jumlah mahasiswanya paling sedikit?
# 2018

#Line chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df1=df['tingkat'].value_counts().rename_axis('tingkat').reset_index(name='counts')
df1=df1.sort_values(["tingkat"],ascending=[0])
df1.plot(kind="line",x="tingkat",y="counts")
plt.savefig("7.png",bbox_inches="tight")

#Line chart seperti soal sebelumnya, namun terdapat 4 garis, masing-masing untuk tiap fakultas.
#df1=df['tingkat'].value_counts()
#plt.savefig("8.png",bbox_inches='tight')
#GABISA

#Berdasar plot sebelumnya, fakultas manakah yang jumlah mahasiswanya terus bertambah?

# Berdasar plot sebelumnya, fakultas manakah yang jumlah mahasiswanya terus berkurang?
