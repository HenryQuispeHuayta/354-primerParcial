# from ._base import load_breast_cancer
# from importlib import resources
# from typing.io import BinaryIO, TextIO

from ast import mod
import numpy as np
import pandas as pd
# from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
# from sklearn import datasets

datos = pd.read_csv('../dataset/high_diamond_ranked_10min.csv')

pd.get_dummies(data=datos, drop_first=True)

a = datos.drop(columns='blueWins')
b = datos.blueWins

# fit()
modelo = DecisionTreeClassifier()

modelo.fit(X=a, y=b)
DecisionTreeClassifier()

plot_tree(decision_tree=modelo, feature_names=a.columns, filled=True)
# print(datos)