import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos = pd.read_csv('../../dataset/high_diamond_ranked_10min.csv')

sns.set_style('darkgrid')
datos2 = datos.copy()
columnas = ['gameId', 'redFirstBlood', 'redKills', 'redEliteMonsters', 'redDragons','redTotalMinionsKilled',
       'redTotalJungleMinionsKilled', 'redGoldDiff', 'redExperienceDiff', 'redCSPerMin', 'redGoldPerMin', 'redHeralds',
       'blueGoldDiff', 'blueExperienceDiff', 'blueCSPerMin', 'blueGoldPerMin', 'blueTotalMinionsKilled']
datos2 = datos2.drop(columnas, axis = 1)

datos2.hist(alpha = 0.7, figsize=(12,10), bins=5)

# plot = datos.plot()

plt.show()