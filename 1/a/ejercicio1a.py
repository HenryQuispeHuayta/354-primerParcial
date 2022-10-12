import numpy as np
import pandas as pd

datos = pd.read_csv('../../dataset/high_diamond_ranked_10min.csv')

def calcular(lista,valor):
  n = len(lista)
  k = ((n)*valor)/100 if(n%2==0) else ((n+1)*valor)/100
  i = int(k).__ceil__()-1
  return lista[columna].sort_values(ignore_index=True)[i] if(k%1==0) else (lista[columna].sort_values(ignore_index=True)[i]+lista[columna].sort_values(ignore_index=True)[i+1])/2

for columna in datos.columns:
  print(columna,':',calcular(datos,25))
  # print(columna,':',np.quantile(datos[columna],0.25))

for columna in datos.columns:
  print(columna,':',calcular(datos,90))
  # print(columna,':',np.percentile(datos[columna],90))

for columna in datos.columns:
  print(columna,':',calcular(datos,95))
  # print(columna,':',np.percentile(datos[columna],95))
