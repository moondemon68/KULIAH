import matplotlib
import pandas as pd
matplotlib.use('agg')
import matplotlib.pyplot as plt

df=pd.read_csv("animal.csv")
df.plot(kind="line",x="Year",y="Bears",title="Line Chart")
plt.savefig("line.png",bbox_inches='tight')

df.plot(kind="bar",x="Year",y="Bears")
plt.savefig("bar.png",bbox_inches='tight')

df.plot(kind="line",x="Year",y=["Bears","Dolphins","Whales"])
plt.savefig("multiline.png",bbox_inches='tight')

df.plot(kind="area",x="Year",y="Bears")
plt.savefig("area.png",bbox_inches="tight")

df.plot(kind="area",x="Year",y=["Bears","Dolphins","Whales"])
plt.savefig("multiarea.png",bbox_inches="tight")

df.plot(kind="scatter",x="Year",y="Bears")
plt.savefig("scatter.png",bbox_inches="tight")

df.plot(kind="scatter",x="Year",y="Bears",sizes=df["Bears"],color="red")
plt.savefig("bubble.png",bbox_inches="tight")

df2=df["Year"].value_counts()
df2.plot(kind="pie")
plt.savefig("pie.png",bbox_inches="tight")
	
df.plot(kind="bar",x="Year",y="Bears",title="Bar Chart")
plt.savefig("bar.png",bbox_inches='tight')

#df.groupby(["Year","Bears"]).size().unstack().plot(kind="line",title="Linegroupby")
#plt.savefig("linegroupby.png",bbox_inches="tight")

#df1=df.groupby(["Year","Bears"]).size().unstack()
#print(df1)
