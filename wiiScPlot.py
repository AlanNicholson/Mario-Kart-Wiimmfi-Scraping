
import matplotlib.pyplot as plt
import pandas as pd


fig = plt.figure()

rect = fig.patch
rect.set_facecolor('white')

df = pd.read_csv('Wiimmfi_Numbers.csv')

graph1 = fig.add_subplot(1, 1, 1, axisbg='white')

graph1.plot()
pd.DataFrame.plot(df)

xAx = list(range(0, len(df['Time'])))
plt.xticks(xAx, df['Time'])
plt.plot(df['Vs. Players'])
plt.plot(df['Room Players'])

plt.axis('auto')
plt.show()