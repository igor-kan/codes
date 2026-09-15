"""Logistic regression with gradient descent."""
import math


def sigmoid(z: float) -> float:
    if z >= 0:
        return 1 / (1 + math.exp(-z))
    return math.exp(z) / (1 + math.exp(z))


def train(features: list[list[float]], labels: list[int], lr=0.1, epochs=1000):
    weights = [0.0] * len(features[0])
    bias = 0.0
    for _ in range(epochs):
        grad_w = [0.0] * len(weights)
        grad_b = 0.0
        for x, y in zip(features, labels):
            prediction = sigmoid(sum(w * xi for w, xi in zip(weights, x)) + bias)
            error = prediction - y
            for j in range(len(weights)):
                grad_w[j] += error * x[j]
            grad_b += error
        n = len(features)
        weights = [w - lr * g / n for w, g in zip(weights, grad_w)]
        bias -= lr * grad_b / n
    return weights, bias


def predict(weights, bias, x) -> int:
    return 1 if sigmoid(sum(w * xi for w, xi in zip(weights, x)) + bias) >= 0.5 else 0


if __name__ == "__main__":
    features = [[0, 0], [0, 1], [1, 0], [1, 1]]
    labels = [0, 1, 1, 1]  # OR gate
    weights, bias = train(features, labels)
    assert [predict(weights, bias, x) for x in features] == labels
    print("logistic regression ok")
