from ast import increment_lineno
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline
# sns.set_style('darkgrid')

datos = pd.read_csv('../../dataset/high_diamond_ranked_10min.csv')
# print(datos)

# print(datos.columns)

# Primer cuartil
for columna in datos.columns:
  print(columna,':', np.quantile(datos[columna], 0.25))

# Percentil 90
for columna in datos.columns:
  print(columna,':', np.percentile(datos[columna], 90))

# Percentil 95
for columna in datos.columns:
  print(columna,':', np.percentile(datos[columna], 95))
# datos.columns