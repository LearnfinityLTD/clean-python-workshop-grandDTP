# messy_analysis.py
# Just some code I wrote to analyze survey data

import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv('data.csv')
d = d.dropna()
d['x'] = d['col1'] * 2
m = d['x'].mean()
print(m)

plt.figure()
plt.plot(d['col1'], d['x'])
plt.show()

r = []
for i in range(len(d)):
    if d.iloc[i]['col1'] > 5:
        r.append(d.iloc[i]['x'])
    
print(len(r))

# Some more calculations
s = 0
for i in range(len(r)):
    s += r[i]
avg = s / len(r)
print(avg)
