from src import pipeline
from src import MLP, TreeClassifier
from src import HIDDEN_LAYER_SIZE, ITER, VERBOSE
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")

X_train, X_test, y_train, y_test = pipeline()
mlp = MLP(HIDDEN_LAYER_SIZE, ITER, VERBOSE)
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy score of MLP Classifier:", format(accuracy*100, '.2f'), "%")


# Training the decision tree classifier
clf = TreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy score of Decision Tree Classifier:", format(accuracy*100, '.2f'), "%")