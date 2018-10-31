import matplotlib
import pandas as pd
matplotlib.use('agg')
import matplotlib.pyplot as plt

df=pd.read_csv("animal.csv")
df.plot(kind="line",x="Year",y="Bears")
plt.savefig("line.png",bbox_inches='tight')

df.plot(kind="bar",x="Year",y="Bears")
plt.savefig("bar.png",bbox_inches='tight')

df.plot(kind="line",x="Year",y=["Bears","Dolphins","Whales"])
plt.savefig("multiline.png",bbox_inches='tight')
