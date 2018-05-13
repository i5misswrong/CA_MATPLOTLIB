import pandas as pd
import matplotlib.pyplot as plt

loca=r'./test.csv'
df=pd.read_csv(loca)
x_axia=df['x_axis'].tolist()
case1=df['case1'].tolist()
case2=df['case2'].tolist()
case3=df['case3'].tolist()

plt.plot(x_axia,case1)
plt.plot(x_axia,case2)
plt.plot(x_axia,case3)
plt.show()


