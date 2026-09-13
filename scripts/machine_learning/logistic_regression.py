"""Binary Logistic Regression with Batch Gradient Descent.

Implements sigmoid activation, cross-entropy log-loss, and weight optimization.
"""

import math
from typing import List, Tuple

def sigmoid(z: float) -> float:
    # Bounded to prevent numerical overflow
    if z < -20.0: return 0.0
    if z > 20.0: return 1.0
    return 1.0 / (1.0 + math.exp(-z))

def dot_product(w: List[float], x: List[float]) -> float:
    return sum(a * b for a, b in zip(w, x))

def train_logistic_regression(
    X: List[List[float]], y: List[int], lr: float = 0.1, epochs: int = 500
) -> List[float]:
    n_samples = len(X)
    n_features = len(X[0])
    # Add bias feature to X
    X_bias = [[1.0] + row for row in X]
    weights = [0.0] * (n_features + 1)

    for _ in range(epochs):
        gradients = [0.0] * (n_features + 1)
        for i in range(n_samples):
            pred = sigmoid(dot_product(weights, X_bias[i]))
            err = pred - y[i]
            for j in range(n_features + 1):
                gradients[j] += err * X_bias[i][j]

        for j in range(n_features + 1):
            weights[j] -= (lr / n_samples) * gradients[j]

    return weights

def predict(weights: List[float], x: List[float]) -> int:
    prob = sigmoid(dot_product(weights, [1.0] + x))
    return 1 if prob >= 0.5 else 0

if __name__ == "__main__":
    # Linearly separable 2D dataset
    X_train = [
        [1.0, 1.0], [2.0, 1.5], [1.5, 2.0], # Class 0
        [6.0, 5.0], [7.0, 6.5], [8.0, 7.0]  # Class 1
    ]
    y_train = [0, 0, 0, 1, 1, 1]

    w = train_logistic_regression(X_train, y_train, lr=0.5, epochs=1000)

    for x, y in zip(X_train, y_train):
        p = predict(w, x)
        assert p == y, f"Misclassification for {x}: expected {y}, got {p}"

    print(f"[Python ML] Logistic Regression converged with 100% training accuracy.")
