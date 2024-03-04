from src import pipeline
from src import MLP
from src import HIDDEN_LAYER_SIZE, ITER, VERBOSE
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")

X_train, X_test, y_train, y_test = pipeline()
mlp = MLP(HIDDEN_LAYER_SIZE, ITER, VERBOSE)
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy score:", accuracy*100)