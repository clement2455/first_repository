import pandas as pd

df = pd.read_csv("Bonjour.txt")

df = df [ ['heure','pseudo'] ]
df = df.sort()

print(df.head())

print('New Bonjour')