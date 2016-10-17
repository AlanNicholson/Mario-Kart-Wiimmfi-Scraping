
import matplotlib.pyplot as plt
import pandas as pd


fig = plt.figure()

rect = fig.patch
rect.set_facecolor('#E6D5FF')

df = pd.read_csv('Wiimmfi_Numbers.csv')

graph1 = fig.add_subplot(1, 1, 1, axisbg='white')

graph1.plot()
pd.DataFrame.plot(df)

xAx = list(range(0, len(df['Time'])))
plt.xticks(xAx, df['Time'])
plt.title('Wiimmfi MarioKart', y=1.08)
plt.xlabel('Time')
plt.ylabel('No. of Players Online')
plt.plot(df['Vs. Players'], color='blue')
plt.plot(df['Room Players'], color='red')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)

plt.axis('auto')
plt.show()
