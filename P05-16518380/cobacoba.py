#IMPORTS
import matplotlib
import pandas as pd
matplotlib.use('agg')
import matplotlib.pyplot as plt

#DATA NO 1
df=pd.read_csv("animal.csv")

df.plot(kind="line",x="Year",y="Bears",title="Line Chart")
plt.savefig("line.png",bbox_inches='tight')

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
	
df.plot(kind="bar",x="Year",y="Bears",title="Bar Chart")
plt.savefig("bar.png",bbox_inches='tight')

df.groupby(["Year","Bears"]).size().unstack().plot(kind="line",title="Linegroupby")
plt.savefig("linegroupby.png",bbox_inches="tight")

#DATA NO 2

df=pd.read_csv("data.csv")

df.plot(kind="bar",x="name",y="age",title="Age of Person")
plt.savefig("bar.png",bbox_inches="tight")

df.plot(kind="bar",x="name",y=["num_children","num_pets"],title="Children vs Pets")
plt.savefig("multibar.png",bbox_inches="tight")

df.plot(kind="barh",x="name",y="age",title="Age of Person")
plt.savefig("barh.png",bbox_inches="tight")

df[["age"]].plot(kind="hist",bins=[0,20,40,60,80,100],rwidth=0.8)
plt.savefig("histo.png",bbox_inches="tight")

df1=df["state"].value_counts()
df1.plot(kind="pie")
plt.savefig("pie.png",bbox_inches="tight")

df1=df.groupby(["gender","state"])["name"].size().unstack()
df1.plot(kind="bar",stacked=True)
plt.savefig("stackedbar.png",bbox_inches="tight")

df1=df.groupby(["gender","state"])["name"].size().unstack()
df1.plot(kind="line",stacked=True)
plt.savefig("stackedline.png",bbox_inches="tight")

