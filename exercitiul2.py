import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv(r"C:\Users\crist\Desktop\ex2\data.csv")

df.plot()
plt.title("Toate valorile")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df[:5].plot(marker="s")
plt.title("Primele 5 valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df1 = df[['Durata' , 'Puls']].head(13)
df1.plot(color=['yellow','blue'])
plt.title("Ultimele 13 valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()