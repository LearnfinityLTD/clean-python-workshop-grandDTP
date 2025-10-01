# Messy script - show this first
import pandas as pd

d = pd.read_csv('survey_data.csv')
d = d.dropna()
d['c'] = d['score'] * 2
m = d['c'].mean()
print(m)

r = []
for i in range(len(d)):
    if d.iloc[i]['score'] > 50:
        r.append(d.iloc[i]['c'])
print(len(r))
