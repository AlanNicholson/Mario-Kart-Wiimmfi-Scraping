
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
plt.plot(df['Vs. Players'], color = 'red')
plt.plot(df['Room Players'], color = 'blue')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)

plt.axis('auto')
plt.show()