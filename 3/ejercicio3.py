import numpy as np
import pandas as pd

from sklearn.preprocessing import KBinsDiscretizer

datos = pd.read_csv('../dataset/high_diamond_ranked_10min.csv')

prepro = KBinsDiscretizer(n_bins=20,encode='ordinal', strategy='uniform')

datos2 = prepro.fit_transform(datos)

print(datos)
print(datos2)