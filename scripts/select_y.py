import pandas as pd

df = pd.read_csv('data/train.csv')
df['IC50, mM'].to_csv('data/ic50.csv')
df['CC50, mM'].to_csv('data/cc50.csv')