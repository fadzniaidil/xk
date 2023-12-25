import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import numpy as np
import pickle
from sklearn.model_selection import train_test_split

df = pandas.read_csv("dataset-1.csv")

d = {'Mechanical': 1, 'EE': 2, 'Chemical': 3, 'Civil': 4, 'IT': 5}
df['Program'] = df['Program'].map(d)

features = ['Melayu', 'Inggeris', 'Matematik', 'Tambahan', 'Kimia', 'Fizik', 'Biologi', 'Sejarah']

X = df[features]
y = df['Program']

X_train, X_test, y_train, y_test, = train_test_split(X, y, test_size=0.3, random_state=1)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
y_pred = dtree.predict(X_test)


pickle.dump(dtree, open('fier.pkl', 'wb'))