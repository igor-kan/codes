"""Perceptron learning algorithm."""
def train(features: list[list[float]], labels: list[int], lr=1.0, epochs=20):
    weights = [0.0] * len(features[0])
    bias = 0.0
    for _ in range(epochs):
        errors = 0
        for x, y in zip(features, labels):
            prediction = 1 if sum(w * xi for w, xi in zip(weights, x)) + bias > 0 else 0
            if prediction != y:
                errors += 1
                for j in range(len(weights)):
                    weights[j] += lr * (y - prediction) * x[j]
                bias += lr * (y - prediction)
        if errors == 0:
            break
    return weights, bias


def predict(weights, bias, x) -> int:
    return 1 if sum(w * xi for w, xi in zip(weights, x)) + bias > 0 else 0


if __name__ == "__main__":
    features = [[0, 0], [0, 1], [1, 0], [1, 1]]
    labels = [0, 0, 0, 1]  # AND gate
    weights, bias = train(features, labels)
    assert [predict(weights, bias, x) for x in features] == labels
    print("perceptron ok")
