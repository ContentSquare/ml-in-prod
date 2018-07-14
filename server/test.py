import dill
from pandas import read_csv

url = "../pima-indians-diabetes.csv"
features = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']
label = 'label'
dataframe = read_csv(url, names=features + [label])
X = dataframe[features]
Y = dataframe[label]

with open('pipeline.pk', 'r') as f:
    clf = dill.load(f)

print clf.score(X, Y)
