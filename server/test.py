import dill
from pandas import read_csv

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
features = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']
label = 'label'
dataframe = read_csv(url, names=features + [label])
X = dataframe[features]
Y = dataframe[label]

with open('../training/pipeline.pk', 'r') as f:
    clf = dill.load(f)

print clf.score(X, Y)
