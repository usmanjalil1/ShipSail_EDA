from sklearn.neural_network import MLPClassifier
from sklearn.base import ClassifierMixin
from sklearn.tree import DecisionTreeClassifier

def MLP(hidden_layer: tuple, iteration: int, verbose: bool) -> ClassifierMixin:
    mlp = MLPClassifier(hidden_layer_sizes=hidden_layer, max_iter=iteration, random_state=42, verbose=verbose)
    return mlp


def TreeClassifier() -> ClassifierMixin:
    dt = DecisionTreeClassifier()
    return dt