"""A tiny MLP with backpropagation trained on XOR."""
import math
import random


def sigmoid(z: float) -> float:
    return 1 / (1 + math.exp(-z))


def sigmoid_prime(output: float) -> float:
    return output * (1 - output)


def train(epochs: int = 60_000, seed: int = 0):
    rng = random.Random(seed)
    w1 = [[rng.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
    b1 = [rng.uniform(-1, 1) for _ in range(2)]
    w2 = [rng.uniform(-1, 1) for _ in range(2)]
    b2 = rng.uniform(-1, 1)
    data = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)]
    lr = 1.0
    for _ in range(epochs):
        for x, y in data:
            hidden = [sigmoid(w1[i][0] * x[0] + w1[i][1] * x[1] + b1[i]) for i in range(2)]
            output = sigmoid(sum(w2[i] * hidden[i] for i in range(2)) + b2)
            d_out = (output - y) * sigmoid_prime(output)
            d_hidden = [d_out * w2[i] * sigmoid_prime(hidden[i]) for i in range(2)]
            for i in range(2):
                w2[i] -= lr * d_out * hidden[i]
            b2 -= lr * d_out
            for i in range(2):
                for j in range(2):
                    w1[i][j] -= lr * d_hidden[i] * x[j]
                b1[i] -= lr * d_hidden[i]
    return w1, b1, w2, b2


def predict(weights, x) -> int:
    w1, b1, w2, b2 = weights
    hidden = [sigmoid(w1[i][0] * x[0] + w1[i][1] * x[1] + b1[i]) for i in range(2)]
    return 1 if sigmoid(sum(w2[i] * hidden[i] for i in range(2)) + b2) >= 0.5 else 0


if __name__ == "__main__":
    weights = train()
    assert [predict(weights, x) for x in ([0, 0], [0, 1], [1, 0], [1, 1])] == [0, 1, 1, 0]
    print("neural network ok")
