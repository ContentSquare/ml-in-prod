import dill
from pandas import read_csv
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn_pandas import DataFrameMapper

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
features = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']
label = 'label'
dataframe = read_csv(url, names=features + [label])
X = dataframe[features]
Y = dataframe[label]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)


def is_adult(x): return x > 18


def is_bigger_than(x, threshold): return x > threshold


clf = Pipeline([
    ("mapper", DataFrameMapper([
        (['age'], FunctionTransformer(is_adult)),
        (features, None)
    ])),
    ("classifier", LogisticRegression())
])

# grid search
params_grid = {'classifier__C': [0.1, 0.5, 1, 5, 10]}
clf = GridSearchCV(clf, params_grid, cv=3, verbose=3, n_jobs=1)

clf.fit(X_train, Y_train)
print clf.score(X_test, Y_test)

with open('../server/pipeline.pk', 'w') as f:
    dill.dump(clf.best_estimator_, f)
