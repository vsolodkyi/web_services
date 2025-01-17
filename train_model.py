from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
np.unique(iris_y)
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)

import joblib
joblib.dump(knn, 'knn.pkl')
