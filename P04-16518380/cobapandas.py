import pandas as pd

df=pd.read_csv("inflasi.csv")
print(df)

#display data
#print(df.loc[4:]) 		#4 sampe abis
#print(df.loc[:10]) 	#0 sampe 10
#print(df.loc[4:10]) 	#4 sampe 10
#print(df.loc[4])		#4 aja

#nyaring data
#df=df.loc[df["Tingkat_Inflasi"]>=5]
#df=df.loc[(df["Tahun"]>=2009) & (df["Tahun"]<=2012)]
#print(df)

#sorting data
#df=df.sort_values(["Tahun","Tingkat_Inflasi"],ascending=[1,0])
#print(df)

#max/min
#maximum=df["Tingkat_Inflasi"].idxmax() #nyimpen index maximum
#minimum=df["Tingkat_Inflasi"].idxmin() #nyimpen index minimum
#print(df.loc[maximum])	#print data maximum	
#print(maximum)			#print index tempat si maximum itu ada

#tabelfrekuensi
#df=df["Tahun"].value_counts()	#print tabel frekuensi
#print(df)

#describe
#df=df["Tahun"].describe()	#print count,mean,stdeviasi,min,25%,50%,75%,max
#print(df)

#korelasi (0=ganyambung,(0,1]=berbandinglurus,[-1,0)=berbanding terbalik
#cor=df["Tingkat_Inflasi"].corr(df["Tahun"])
#print(cor)
